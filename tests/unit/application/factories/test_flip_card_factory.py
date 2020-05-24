from unittest import TestCase

from src.application.factories.flip_card_factory import FlipCardFactory
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.flip_card_id import FlipCardId
from src.domain.vos.flip_card_side_id import FlipCardSideId
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubFrontPolish, Sentence_StubBackEnglish


class TestFlipCardFactory(TestCase):
    def test_flip_card_creation__return_flip_card(self):
        sentence_front_stub = Sentence_StubBackEnglish()
        sentence_back_stub = Sentence_StubFrontPolish()

        flip_card = FlipCardFactory.create_card(front_sentence=sentence_front_stub, back_sentence=sentence_back_stub)

        self.assertIsInstance(flip_card, FlipCard)
        self.assertIsInstance(flip_card.id_, FlipCardId)
        self.assertIsInstance(flip_card._front.id_, FlipCardSideId)
        self.assertEqual(flip_card._front.sentence.value, sentence_front_stub.value)
        self.assertIsInstance(flip_card._back.id_, FlipCardSideId)
        self.assertEqual(flip_card._back.sentence.value, sentence_back_stub.value)
