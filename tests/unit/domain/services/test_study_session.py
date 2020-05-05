from abc import ABC, abstractmethod
from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.services.new_card_picker import NewCardPicker, NewCardPickerInterface
from src.domain.vos.abstractions.value_object import ValueObject
from src.domain.vos.card_side_state import CardSideState
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardNewStub


# TODO WIP

class NewCardBufferInterface(ABC):
    @abstractmethod
    def append(self, flip_card: FlipCard):
        pass


class NewCardBufferSpy(NewCardBufferInterface):
    def __init__(self):
        self.call_stack = []

    def append(self, flip_card: FlipCard):
        self.call_stack.append((self.append.__name__, flip_card))


class NewCardPickerStub(NewCardPickerInterface):
    def draw_new_card(self):
        return FlipCardNewStub()


class Answer(ValueObject):
    def _validate_value(self, value: str):
        if not isinstance(value, str):
            raise self.InvalidAnswerFormat()

    class InvalidAnswerFormat(Exception):
        pass


class StudySession:
    def __init__(self, buffer: NewCardBufferInterface, new_card_picker: NewCardPickerInterface):
        self.buffer = buffer
        self.new_card_picker = new_card_picker

    def start(self) -> FlipCard:
        return self.new_card_picker.draw_new_card()

    def advance(self, flip_card: FlipCard, answer: Answer) -> FlipCard:
        self.buffer.append(flip_card)

        return self.new_card_picker.draw_new_card()


class TestStudySession(TestCase):
    def setUp(self):
        self.study_session = StudySession(NewCardBufferSpy(), NewCardPickerStub())

    def test_first_draw__return_new_card(self):
        flip_card = self.study_session.start()

        self.assertIsInstance(flip_card, FlipCard)

    def test_user_does_not_know_card__put_card_in_new_cards_buffer__return_next_card(self):
        flip_card = FlipCardNewStub()
        flip_card.front_state = CardSideState(CardSideState.StateType.DRAWN)

        next_flip_card = self.study_session.advance(flip_card=flip_card)

        self.assertIsInstance(next_flip_card, FlipCard)
        self._assert_answer_got_submitted_for_verification()
        self._assert_card_got_put_in_buffer(flip_card)

    def _assert_card_got_put_in_buffer(self, flip_card: FlipCard):
        call_stack = self.study_session.buffer.call_stack
        called_method = NewCardBufferInterface.append.__name__

        self.assertTupleEqual(call_stack[0], (called_method, flip_card))

    def _assert_answer_got_submitted_for_verification(self, answer: Answer):
        call_stack = self.answer_verifier.buffer.call_stack
        called_method = AnswerVerifier.check.__name__

        self.assertTupleEqual(call_stack[0], (called_method, answer))