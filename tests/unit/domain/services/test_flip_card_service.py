from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.events.new_card_created import NewCardCreated
from src.domain.services.flip_card_service import FlipCardService
from tests.unit.domain.events_log_spy import EventLogSpy
from tests.unit.application.factories.test_doubles.flip_card_factory_spy import FlipCardFactorySpy
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardsRepositorySpy
from tests.unit.domain.vos.test_doubles.sentence_back_stub import SentenceBackStub
from tests.unit.domain.vos.test_doubles.sentence_front_stub import SentenceFrontStub


class TestFlipCardService(TestCase):
    def setUp(self):
        self.events_log = EventLogSpy()
        self.repository = FlipCardsRepositorySpy()
        self.flip_card_service = FlipCardService(events_log=self.events_log, repository=self.repository)

    def test_adding_flip_card__emit_added_card_event(self):
        sentence_front = SentenceFrontStub()
        sentence_back = SentenceBackStub()
        factory = FlipCardFactorySpy()

        self.flip_card_service.create_card(front=sentence_front, back=sentence_back, factory=factory)

        self.assertTupleEqual(factory.call_stack[0],
                              (factory.create_card.__name__, [sentence_front, sentence_back]))
        self.assertTupleEqual(self.repository.call_stack[0],
                              (self.repository.save.__name__, FlipCardFactorySpy.flip_card_stub))
        self.assertEqual(self.events_log.call_stack[0][0], self.events_log.register.__name__)
        self.assertIsInstance(self.events_log.call_stack[0][1], NewCardCreated)

    def test_drawing_a_card__return_a_random_card(self):
        flip_card = self.flip_card_service.draw_a_card()

        self.assertIsInstance(flip_card, FlipCard)
