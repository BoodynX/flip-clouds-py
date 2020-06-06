from unittest import TestCase

from src.application.factories.flip_card_factory import FlipCardFactory
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_id import FlipCardId
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubFrontPolish, Sentence_StubBackEnglish


class TestFlipCardFactory(TestCase):
    def test_flip_card_creation__return_flip_card(self):
        sentence_front_stub = Sentence_StubBackEnglish()
        sentence_back_stub = Sentence_StubFrontPolish()

        flip_card = FlipCardFactory.create_card(front=sentence_front_stub, back=sentence_back_stub)

        self.assertIsInstance(flip_card, FlipCard)
        self.assertIsInstance(flip_card.id_, FlipCardId)
        self.assertEqual(flip_card.front.value, sentence_front_stub.value)
        self.assertEqual(flip_card.back.value, sentence_back_stub.value)
