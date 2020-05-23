# from abc import ABC, abstractmethod
# from unittest import TestCase
#
# from src.domain.entities.flip_card import FlipCard
# from src.domain.events.abstractions.event import Event
# from src.domain.services.event_log.event_log import EventLog
# from src.domain.services.new_card_picker import NewCardPickerInterface
# from src.domain.vos.abstractions.value_object import ValueObject
# from src.domain.vos.card_side_state import CardSideState
# from src.domain.vos.sentence import Sentence
# from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCard_StubAllNew
# from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLog_Spy
#
#
#
# class NewFlipCardBoxInterface(ABC):
#     @abstractmethod
#     def append(self, flip_card: FlipCard):
#         """
#         Append the whole card to check what is going on with the other side.
#         If it's new you need to add it to the secondary _box,
#         so that it gets drawn later.
#         """
#
#
# class NewFlipCardBoxSpy(NewFlipCardBoxInterface):
#     def __init__(self):
#         self.call_stack = []
#
#     def append(self, flip_card: FlipCard):
#         self.call_stack.append((self.append.__name__, flip_card))
#
#
# class NewCardPickerStub(NewCardPickerInterface):
#     def draw_new_card(self):
#         return FlipCard_StubAllNew()
#
#
# class Answer(ValueObject):
#     valid_pattern = Sentence.valid_pattern
#
#     def _validate_value(self, value: str):
#         if not value:
#             raise self.InvalidAnswerFormat()
#         value = value.strip()
#         if not self.valid_pattern.match(value):
#             raise self.InvalidAnswerFormat()
#
#     class InvalidAnswerFormat(Exception):
#         pass
#
#
# class AnswerChecked(Event):
#     def __init__(self, result: bool):
#         self.result = result
#
#
# class StudySession:
#     def __init__(self, event_log: EventLog,
#                  container: NewFlipCardBoxInterface,
#                  new_card_picker: NewCardPickerInterface):
#         self.event_log = event_log
#         self._box = container
#         self.new_card_picker = new_card_picker
#
#     def draw_new_card(self) -> FlipCard:
#         return self.new_card_picker.draw_new_card()
#
#     # def submit_answer(self, answer: Answer, flip_card: FlipCard):
#     #     flip_card
#     #     if answer:
#     #         self._box.append(flip_card=flip_card)
#     #         self.event_log.fire(event=AnswerChecked(False))
#
#
# class AnswerDummy(Answer):
#     def __init__(self):
#         """pass"""
#
#
# class TestStudySessionNewCards(TestCase):
#     def setUp(self):
#         self.event_log = EventLog_Spy()
#         self.new_flip_card_box = NewFlipCardBoxSpy()
#         self.new_card_picker = NewCardPickerStub()
#         self.study_session = StudySession(self.event_log, self.new_flip_card_box, self.new_card_picker)
#         self.flip_card = FlipCard_StubAllNew()
#         self.answer = AnswerDummy()
#
#     def test_first_draw__return_new_card(self):
#         flip_card = self.study_session.draw_new_card()
#
#         self.assertIsInstance(flip_card, FlipCard)
#
#     def test_user_submits_wrong_answer__put_card_in_new_cards_box__fire_event(self):
#         self.flip_card.front_state = CardSideState(CardSideState.StateType.DRAWN)
#
#         # self.study_session.submit_answer(answer=self.answer, flip_card=self.flip_card)
#
#     #     self._assert_answer_got_submitted_for_verification()
#     #     self._assert_card_got_put_in_box()
#     #     self._assert_event_fired__answer_checked__wrong_answer()
#     #
#     # def _assert_answer_got_submitted_for_verification(self):
#     #     call_stack = self.answer_verifier.call_stack
#     #     called_method = self.answer_verifier.check.__name__
#     #
#     #     self.assertTupleEqual(call_stack[0], (called_method, self.answer))
#     #
#     # def _assert_card_got_put_in_box(self):
#     #     call_stack = self.study_session._box.call_stack
#     #     called_method = NewFlipCardBoxInterface.append.__name__
#     #
#     #     self.assertTupleEqual(call_stack[0], (called_method, self.flip_card))
#     #
#     # def _assert_event_fired__answer_checked__wrong_answer(self):
#     #     call_stack = self.event_log.call_stack
#     #     called_method = call_stack[0][0]
#     #     expected_method_call = self.event_log.fire.__name__
#     #     fired_event = call_stack[0][1]
#     #
#     #     self.assertEqual(called_method, expected_method_call)
#     #     self.assertIsInstance(fired_event, AnswerChecked)
#     #     self.assertFalse(fired_event.result)
#
#
#
# class TestStudySessionDayPlan(TestCase):
#     """pass"""
