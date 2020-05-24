from unittest import TestCase

from src.domain.entities.flip_card_side import FlipCardSide
from src.domain.services.new_flip_card_side_picker import NewFlipCardSidePicker
from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLog_Spy
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardsRepository_Spy


class TestNewFlipCardSidePicker(TestCase):
    def setUp(self):
        self.event_log = EventLog_Spy()

    def test_drawing_new_card_from_all_unknown_cards__return_flip_card(self):
        repository = FlipCardsRepository_Spy()
        new_card_picker = NewFlipCardSidePicker(event_log=self.event_log, repository=repository)
        flip_card_side = new_card_picker.draw_new_card_side()

        self.assertIsInstance(flip_card_side, FlipCardSide)
