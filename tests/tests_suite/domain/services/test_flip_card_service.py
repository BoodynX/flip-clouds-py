from unittest import TestCase

from src.domain.events.new_card_created import NewCardCreated
from src.domain.services.flip_card_service import FlipCardService
from tests.test_doubles.domain.factories.flip_card_factory_spy import FlipCardFactorySpy
from tests.test_doubles.domain.vos.sentence_back_stub import SentenceBackStub
from tests.test_doubles.domain.vos.sentence_front_stub import SentenceFrontStub
from tests.test_doubles.domain.events_log_spy import EventLogSpy


class TestFlipCardService(TestCase):
    def test_adding_flip_card__emit_added_card_event(self):
        events_log = EventLogSpy()
        flip_card_service = FlipCardService(events_log=events_log)
        sentence_front = SentenceFrontStub()
        sentence_back = SentenceBackStub()
        flip_card_factory = FlipCardFactorySpy()

        flip_card_service.create_card(front=sentence_front, back=sentence_back, factory=flip_card_factory)

        self.assertListEqual(flip_card_factory.calls_stack[0], [sentence_front, sentence_back])
        self.assertIsInstance(events_log.calls_stack[0], NewCardCreated)
