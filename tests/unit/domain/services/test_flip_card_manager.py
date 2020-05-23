from unittest import TestCase

from src.domain.events.new_card_created import NewCardCreated
from src.domain.services.flip_card_manager import FlipCardManager
from tests.unit.application.factories.test_doubles.flip_card_factory_spy import FlipCardFactory_Spy
from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLog_Spy
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubFrontPolish, Sentence_StubBackEnglish
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardsRepository_Spy


class TestFlipCardManager(TestCase):
    def setUp(self):
        self.event_log = EventLog_Spy()

    def test_adding_flip_card__emit_added_card_event(self):
        sentence_front = Sentence_StubBackEnglish()
        sentence_back = Sentence_StubFrontPolish()
        factory = FlipCardFactory_Spy.get_fresh_spy()
        repository = FlipCardsRepository_Spy()
        flip_card_manager = FlipCardManager(event_log=self.event_log, repository=repository)

        flip_card_manager.create_card(front=sentence_front, back=sentence_back, factory=factory)

        self.assertTupleEqual(factory.call_stack[0],
                              (factory.create_card.__name__, (sentence_front, sentence_back)))
        self.assertTupleEqual(repository.call_stack[0],
                              (repository.save.__name__, FlipCardFactory_Spy.flip_card_stub))
        self.assertEqual(self.event_log.call_stack[0][0], self.event_log.fire.__name__)
        self.assertIsInstance(self.event_log.call_stack[0][1], NewCardCreated)
