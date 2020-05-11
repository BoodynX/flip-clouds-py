from abc import ABC, abstractmethod
from unittest import TestCase

from src.domain.entities.buffer import Buffer, BufferInterface
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_side_id import FlipCardSideId
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardStubFrontDrawn
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateStubPlanned


class BufferRepositoryInterface(ABC):
    @abstractmethod
    def save_buffer_state(self, buffer: Buffer):
        """pass"""

    @abstractmethod
    def get_buffer_state(self) -> Buffer:
        """pass"""


class BufferSpy(BufferInterface):
    def __init__(self):
        self.call_stack = []

    def add_to_primary(self, flip_card_side_id: FlipCardSideId):
        self.call_stack.append((self.add_to_primary.__name__, flip_card_side_id))

    def add_to_secondary(self, flip_card_side_id: FlipCardSideId):
        self.call_stack.append((self.add_to_secondary.__name__, flip_card_side_id))


class BufferRepositorySpy(BufferRepositoryInterface):
    def __init__(self):
        self.call_stack = []
        self.buffer_spy = BufferSpy()

    def save_buffer_state(self, buffer: Buffer):
        self.call_stack.append((self.save_buffer_state.__name__, buffer))

    def get_buffer_state(self) -> BufferInterface:
        self.call_stack.append((self.get_buffer_state.__name__,))
        return self.buffer_spy


class BufferManager:
    def __init__(self, repository: BufferRepositoryInterface):
        self._repository = repository

    def add_card(self, flip_card: FlipCard):
        drawn_side_id = flip_card.get_drawn_side_id()

        if not drawn_side_id:
            raise self.SubmittedCardWasNotDrawn()

        opposite_side = flip_card.get_opposite_side_id_to(side_id=drawn_side_id)

        buffer = self._repository.get_buffer_state()
        buffer.add_to_primary(flip_card_side_id=drawn_side_id)

        # if opposite_side.
        buffer.add_to_secondary(flip_card_side_id=opposite_side)

        self._repository.save_buffer_state(buffer=buffer)

    class SubmittedCardWasNotDrawn(Exception):
        """pass"""


class TestNewCardsBufferManager(TestCase):
    def setUp(self) -> None:
        self.buffer_repository = BufferRepositorySpy()
        self.buffer_manager = BufferManager(repository=self.buffer_repository)
        self.flip_card = FlipCardStubFrontDrawn()

    def test_add_new_card_side_to_buffer__drawn_side_in_primary_and_other_side_in_secondary(self):
        self.buffer_manager.add_card(self.flip_card)

        self._assert_buffer_state_fetched()
        self._assert_drawn_side_added_to_primary_buffer()
        self._assert_other_side_added_to_secondary_buffer()
        self._assert_buffer_state_saved()

    # def test_add_half_planned_cards_drawn_side_to_buffer__drawn_side_in_primary(self):
    #     self.flip_card.back_state = CardSideStateStubPlanned()
    #
    #     self.buffer_manager.add_card(self.flip_card)
    #
    #     self._assert_buffer_state_fetched()
    #     self._assert_drawn_side_added_to_primary_buffer()
    #     self._assert_other_side_not_added_to_secondary_buffer()
    #     self._assert_buffer_state_saved() # TODO Continue...

    def _assert_buffer_state_saved(self):
        called_method = self.buffer_repository.call_stack[1][0]
        expected_method_call = BufferRepositoryInterface.save_buffer_state.__name__

        self.assertEqual(called_method, expected_method_call)

    def _assert_drawn_side_added_to_primary_buffer(self):
        buffer_stack = self.buffer_repository.buffer_spy.call_stack

        called_method = buffer_stack[0][0]
        expected_method_call = Buffer.add_to_primary.__name__
        submitted_value = buffer_stack[0][1]

        self.assertEqual(called_method, expected_method_call)
        self.assertEqual(submitted_value, self.flip_card.front_id)

    def _assert_other_side_added_to_secondary_buffer(self):
        buffer_stack = self.buffer_repository.buffer_spy.call_stack

        called_method = buffer_stack[1][0]
        expected_method_call = Buffer.add_to_secondary.__name__
        submitted_value = buffer_stack[1][1]

        self.assertEqual(called_method, expected_method_call)
        self.assertEqual(submitted_value, self.flip_card.back_id)

    def _assert_buffer_state_fetched(self):
        called_method = self.buffer_repository.call_stack[0][0]
        called_method_name = BufferRepositoryInterface.get_buffer_state.__name__

        self.assertEqual(called_method, called_method_name)

    def _assert_other_side_not_added_to_secondary_buffer(self):
        buffer_stack = self.buffer_repository.buffer_spy.call_stack

        called_method = buffer_stack[0][0]
        not_expected_method_call = Buffer.add_to_secondary.__name__

        self.assertEqual(len(buffer_stack), 1)
        self.assertNotEqual(called_method, not_expected_method_call)
