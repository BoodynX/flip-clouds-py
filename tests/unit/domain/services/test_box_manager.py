from abc import ABC, abstractmethod
from unittest import TestCase

from src.domain.entities.box import Box, BoxInterface
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_side_id import FlipCardSideId
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardStubFrontDrawn
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateStubPlanned


class BoxRepositoryInterface(ABC):
    @abstractmethod
    def save_box_state(self, box: Box):
        """pass"""

    @abstractmethod
    def get_box_state(self) -> Box:
        """pass"""


class BoxSpy(BoxInterface):
    def __init__(self):
        self.call_stack = []

    def add_to_primary(self, flip_card_side_id: FlipCardSideId):
        self.call_stack.append((self.add_to_primary.__name__, flip_card_side_id))

    def add_to_secondary(self, flip_card_side_id: FlipCardSideId):
        self.call_stack.append((self.add_to_secondary.__name__, flip_card_side_id))


class BoxRepositorySpy(BoxRepositoryInterface):
    def __init__(self):
        self.call_stack = []
        self.box_spy = BoxSpy()

    def save_box_state(self, box: Box):
        self.call_stack.append((self.save_box_state.__name__, box))

    def get_box_state(self) -> BoxInterface:
        self.call_stack.append((self.get_box_state.__name__,))
        return self.box_spy


class BoxManager:
    def __init__(self, repository: BoxRepositoryInterface):
        self._repository = repository

    def add_card(self, flip_card: FlipCard):
        drawn_side_id = flip_card.get_drawn_side()

        if not drawn_side_id:
            raise self.SubmittedCardWasNotDrawn()

        opposite_side = flip_card.get_opposite_side_to(side=drawn_side_id)

        box = self._repository.get_box_state()
        box.add_to_primary(flip_card_side_id=drawn_side_id)

        # if opposite_side.
        box.add_to_secondary(flip_card_side_id=opposite_side)

        self._repository.save_box_state(box=box)

    class SubmittedCardWasNotDrawn(Exception):
        """pass"""


class TestNewCardsBoxManager(TestCase):
    def setUp(self) -> None:
        self.box_repository = BoxRepositorySpy()
        self.box_manager = BoxManager(repository=self.box_repository)
        self.flip_card = FlipCardStubFrontDrawn()

    def test_add_new_card_side_to_box__drawn_side_in_primary_and_other_side_in_secondary(self):
        self.box_manager.add_card(self.flip_card)

        self._assert_box_state_fetched()
        self._assert_drawn_side_added_to_primary_box()
        self._assert_other_side_added_to_secondary_box()
        self._assert_box_state_saved()

    # def test_add_half_planned_cards_drawn_side_to_box__drawn_side_in_primary(self):
    #     self.flip_card.back_state = CardSideStateStubPlanned()
    #
    #     self.box_manager.add_card(self.flip_card)
    #
    #     self._assert_box_state_fetched()
    #     self._assert_drawn_side_added_to_primary_box()
    #     self._assert_other_side_not_added_to_secondary_box()
    #     self._assert_box_state_saved() # TODO Continue...

    def _assert_box_state_saved(self):
        called_method = self.box_repository.call_stack[1][0]
        expected_method_call = BoxRepositoryInterface.save_box_state.__name__

        self.assertEqual(called_method, expected_method_call)

    def _assert_drawn_side_added_to_primary_box(self):
        box_stack = self.box_repository.box_spy.call_stack

        called_method = box_stack[0][0]
        expected_method_call = Box.add_to_primary.__name__
        submitted_value = box_stack[0][1]

        self.assertEqual(called_method, expected_method_call)
        self.assertEqual(submitted_value, self.flip_card.front_id)

    def _assert_other_side_added_to_secondary_box(self):
        box_stack = self.box_repository.box_spy.call_stack

        called_method = box_stack[1][0]
        expected_method_call = Box.add_to_secondary.__name__
        submitted_value = box_stack[1][1]

        self.assertEqual(called_method, expected_method_call)
        self.assertEqual(submitted_value, self.flip_card.back.id_)

    def _assert_box_state_fetched(self):
        called_method = self.box_repository.call_stack[0][0]
        called_method_name = BoxRepositoryInterface.get_box_state.__name__

        self.assertEqual(called_method, called_method_name)

    def _assert_other_side_not_added_to_secondary_box(self):
        box_stack = self.box_repository.box_spy.call_stack

        called_method = box_stack[0][0]
        not_expected_method_call = Box.add_to_secondary.__name__

        self.assertEqual(len(box_stack), 1)
        self.assertNotEqual(called_method, not_expected_method_call)
