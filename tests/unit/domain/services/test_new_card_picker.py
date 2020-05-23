from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.services.new_card_picker import NewCardPicker
from src.domain.vos.card_side_state import CardSideState
from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLogSpy
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import \
    FlipCardsRepositoryNewCardSpy, FlipCardsRepositoryFrontPlannedCardSpy, FlipCardsRepositoryBackPlannedCardSpy


class TestNewCardPicker(TestCase):
    def setUp(self):
        self.event_log = EventLogSpy()

    def test_drawing_new_card_from_all_unknown_cards__return_flip_card_with_one_drawn_side(self):
        repository = FlipCardsRepositoryNewCardSpy()
        new_card_picker = NewCardPicker(event_log=self.event_log, repository=repository)
        flip_card = new_card_picker.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
        self._assert_one_side_only_is_drawn(flip_card)

    def test_drawing_front_planned_card_from_all_unknown_cards__return_flip_card_with_one_drawn_side(self):
        repository = FlipCardsRepositoryFrontPlannedCardSpy()
        new_card_picker = NewCardPicker(event_log=self.event_log, repository=repository)
        flip_card = new_card_picker.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
        self._assert_one_side_only_is_drawn(flip_card)

    def test_drawing_back_planned_card_from_all_unknown_cards__return_flip_card_with_one_drawn_side(self):
        repository = FlipCardsRepositoryBackPlannedCardSpy()
        new_card_picker = NewCardPicker(event_log=self.event_log, repository=repository)
        flip_card = new_card_picker.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
        self._assert_one_side_only_is_drawn(flip_card)

    def _assert_one_side_only_is_drawn(self, flip_card):
        self.assertTrue(
            flip_card.back_state == CardSideState.StateType.DRAWN
            or flip_card.front_state == CardSideState.StateType.DRAWN
        )
        self.assertFalse(
            flip_card.back_state == CardSideState.StateType.DRAWN
            and flip_card.front_state == CardSideState.StateType.DRAWN
        )
