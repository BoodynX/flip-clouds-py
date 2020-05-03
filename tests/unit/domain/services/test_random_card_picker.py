from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.services.random_card_picker import RandomCardPicker
from src.domain.vos.card_side_state import CardSideState
from tests.unit.domain.entities.test_doubles.day_plan_stub import DayPlanStub
from tests.unit.domain.event_log_spy import EventLogSpy
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import \
    FlipCardsRepositoryNewCardSpy, FlipCardsRepositoryFrontPlannedCardSpy, FlipCardsRepositoryBackPlannedCardSpy


class TestRandomCardPicker(TestCase):
    def setUp(self):
        self.event_log = EventLogSpy()

    def test_drawing_new_card_from_all_unknown_cards__return_flip_card_with_one_drawn_side(self):
        repository = FlipCardsRepositoryNewCardSpy()
        random_card_picker = RandomCardPicker(event_log=self.event_log, repository=repository)
        flip_card = random_card_picker.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
        self._assert_one_side_only_is_drawn(flip_card)

    def test_drawing_front_planned_card_from_all_unknown_cards__return_flip_card_with_one_drawn_side(self):
        repository = FlipCardsRepositoryFrontPlannedCardSpy()
        random_card_picker = RandomCardPicker(event_log=self.event_log, repository=repository)
        flip_card = random_card_picker.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
        self._assert_one_side_only_is_drawn(flip_card)

    def test_drawing_back_planned_card_from_all_unknown_cards__return_flip_card_with_one_drawn_side(self):
        repository = FlipCardsRepositoryBackPlannedCardSpy()
        random_card_picker = RandomCardPicker(event_log=self.event_log, repository=repository)
        flip_card = random_card_picker.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
        self._assert_one_side_only_is_drawn(flip_card)

    def test_drawing_random_card_from_day_plan__return_flip_card(self):
        day_plan = DayPlanStub()
        repository = FlipCardsRepositoryNewCardSpy()
        random_card_picker = RandomCardPicker(event_log=self.event_log, repository=repository)

        flip_card = random_card_picker.draw_card_from_plan(day_plan=day_plan)

        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(repository.call_stack[0][0], repository.get_by_side_id.__name__)
        self.assertIn(repository.call_stack[0][1], day_plan.flip_card_side_ids)

    def _assert_one_side_only_is_drawn(self, flip_card):
        self.assertTrue(
            flip_card.back_state == CardSideState.StateType.DRAWN
            or flip_card.front_state == CardSideState.StateType.DRAWN
        )
        self.assertFalse(
            flip_card.back_state == CardSideState.StateType.DRAWN
            and flip_card.front_state == CardSideState.StateType.DRAWN
        )
