from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.services.new_card_picker import NewCardPicker
from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLog_Spy
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardsRepository_Spy


class TestNewCardPicker(TestCase):
    def setUp(self):
        self.event_log = EventLog_Spy()

    def test_drawing_new_card_from_all_unknown_cards__return_flip_card(self):
        repository = FlipCardsRepository_Spy()
        new_card_picker = NewCardPicker(event_log=self.event_log, repository=repository)
        flip_card = new_card_picker.draw_new_card()

        self.assertIsInstance(flip_card, FlipCard)
