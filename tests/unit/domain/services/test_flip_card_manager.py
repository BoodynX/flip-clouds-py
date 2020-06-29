from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.events.new_card_created import NewCardCreated
from src.domain.services.flip_card_manager import FlipCardManager
from tests.unit.application.factories.test_doubles.flip_card_factory_spy import FlipCardFactory_Spy
from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLog_Spy
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubFrontPolish, Sentence_StubBackEnglish
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardRepository_Spy


class TestFlipCardManager(TestCase):
    def setUp(self):
        self.event_log = EventLog_Spy()

    def test_adding_flip_card__emit_added_card_event(self):
        self.sentence_front = Sentence_StubBackEnglish()
        self.sentence_back = Sentence_StubFrontPolish()
        factory = FlipCardFactory_Spy.get_fresh_spy()
        repository = FlipCardRepository_Spy()
        flip_card_manager = FlipCardManager(event_log=self.event_log, repository=repository)

        flip_card = flip_card_manager.create_card(front=self.sentence_front, back=self.sentence_back, factory=factory)

        self._assert_factory_called(factory)
        self._assert_card_saved_to_repository(repository)
        self._assert_new_card_created_event_fired()
        self._assert_correct_clip_card_returned(flip_card)

    def _assert_new_card_created_event_fired(self):
        self.assertEqual(self.event_log.call_stack[0][0], self.event_log.fire.__name__)
        self.assertIsInstance(self.event_log.call_stack[0][1], NewCardCreated)

    def _assert_card_saved_to_repository(self, repository):
        self.assertTupleEqual(repository.call_stack[0],
                              (repository.save.__name__, FlipCardFactory_Spy.flip_card_stub))

    def _assert_factory_called(self, factory):
        self.assertTupleEqual(factory.call_stack[0],
                              (factory.create_card.__name__, (self.sentence_front, self.sentence_back)))

    def _assert_correct_clip_card_returned(self, flip_card):
        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(flip_card.front, self.sentence_front)
        self.assertEqual(flip_card.back, self.sentence_back)
