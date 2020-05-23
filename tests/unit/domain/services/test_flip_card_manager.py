from unittest import TestCase

from src.domain.events.new_card_created import NewCardCreated
from src.domain.services.flip_card_manager import FlipCardManager
from tests.unit.application.factories.test_doubles.flip_card_factory_spy import FlipCardFactorySpy
from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLogSpy
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceStubPolish, SentenceStubEnglish
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardsRepositorySpy


class TestFlipCardManager(TestCase):
    def setUp(self):
        self.event_log = EventLogSpy()

    def test_adding_flip_card__emit_added_card_event(self):
        sentence_front = SentenceStubEnglish()
        sentence_back = SentenceStubPolish()
        factory = FlipCardFactorySpy.get_fresh_spy()
        repository = FlipCardsRepositorySpy()
        flip_card_manager = FlipCardManager(event_log=self.event_log, repository=repository)

        flip_card_manager.create_card(front=sentence_front, back=sentence_back, factory=factory)

        self.assertTupleEqual(factory.call_stack[0],
                              (factory.create_card.__name__, (sentence_front, sentence_back)))
        self.assertTupleEqual(repository.call_stack[0],
                              (repository.save.__name__, FlipCardFactorySpy.flip_card_stub))
        self.assertEqual(self.event_log.call_stack[0][0], self.event_log.fire.__name__)
        self.assertIsInstance(self.event_log.call_stack[0][1], NewCardCreated)
