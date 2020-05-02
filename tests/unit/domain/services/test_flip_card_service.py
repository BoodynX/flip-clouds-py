from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.events.new_card_created import NewCardCreated
from src.domain.services.flip_card_service import FlipCardService
from src.domain.vos.card_side_state import CardSideState
from tests.unit.application.factories.test_doubles.flip_card_factory_spy import FlipCardFactorySpy
from tests.unit.domain.entities.test_doubles.day_plan_stub import DayPlanStub
from tests.unit.domain.event_log_spy import EventLogSpy
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceBackStub, SentenceFrontStub
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardsRepositoryNewCardSpy, \
    FlipCardsRepositorySpy, FlipCardsRepositoryHalfPlannedCardSpy


class TestFlipCardService(TestCase):
    def setUp(self):
        self.event_log = EventLogSpy()

    def test_adding_flip_card__emit_added_card_event(self):
        sentence_front = SentenceFrontStub()
        sentence_back = SentenceBackStub()
        factory = FlipCardFactorySpy
        repository = FlipCardsRepositorySpy()
        flip_card_service = FlipCardService(event_log=self.event_log, repository=repository)

        flip_card_service.create_card(front=sentence_front, back=sentence_back, factory=factory)

        self.assertTupleEqual(factory.call_stack[0],
                              (factory.create_card.__name__, (sentence_front, sentence_back)))
        self.assertTupleEqual(repository.call_stack[0],
                              (repository.save.__name__, FlipCardFactorySpy.flip_card_stub))
        self.assertEqual(self.event_log.call_stack[0][0], self.event_log.register.__name__)
        self.assertIsInstance(self.event_log.call_stack[0][1], NewCardCreated)

    def test_drawing_new_card_from_all_unknown_cards__return_flip_card_with_one_drawn_side(self):
        repository = FlipCardsRepositoryNewCardSpy()
        flip_card_service = FlipCardService(event_log=self.event_log, repository=repository)
        flip_card = flip_card_service.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
        self._assert_one_side_only_is_drawn(flip_card)

    def test_drawing_half_planned_card_from_all_unknown_cards__return_flip_card_with_one_drawn_side(self):
        repository = FlipCardsRepositoryHalfPlannedCardSpy()
        flip_card_service = FlipCardService(event_log=self.event_log, repository=repository)
        flip_card = flip_card_service.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
        self._assert_one_side_only_is_drawn(flip_card)

    def test_drawing_random_card_from_day_plan__return_flip_card(self):
        day_plan = DayPlanStub()
        repository = FlipCardsRepositoryNewCardSpy()
        flip_card_service = FlipCardService(event_log=self.event_log, repository=repository)

        flip_card = flip_card_service.draw_card_from_plan(day_plan=day_plan)

        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(repository.call_stack[0][0], repository.get.__name__)
        self.assertIn(repository.call_stack[0][1], day_plan.flip_card_ids)

    def _assert_one_side_only_is_drawn(self, flip_card):
        self.assertTrue(
            flip_card.back_state == CardSideState.StateType.DRAWN
            or flip_card.front_state == CardSideState.StateType.DRAWN
        )
        self.assertFalse(
            flip_card.back_state == CardSideState.StateType.DRAWN
            and flip_card.front_state == CardSideState.StateType.DRAWN
        )
