from unittest import TestCase

from src.application.factories.flip_card_factory import FlipCardFactory
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_id import FlipCardId
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceBackStub, SentenceFrontStub


class TestFlipCardFactory(TestCase):
    def test_flip_card_creation__return_flip_card(self):
        front_stub = SentenceFrontStub()
        back_stub = SentenceBackStub()

        flip_card = FlipCardFactory.create_card(front=front_stub, back=back_stub)

        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(flip_card.front.value, front_stub.value)
        self.assertEqual(flip_card.back.value, back_stub.value)
        self.assertIsInstance(flip_card.id_, FlipCardId)
