from unittest import TestCase

from src.application.factories.flip_card_factory import FlipCardFactory
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.flip_card_id import FlipCardId
from src.domain.vos.flip_card_side_id import FlipCardSideIdBack, FlipCardSideIdFront
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceStubBack, SentenceStubFront


class TestFlipCardFactory(TestCase):
    def test_flip_card_creation__return_flip_card(self):
        front_stub = SentenceStubFront()
        back_stub = SentenceStubBack()

        flip_card = FlipCardFactory.create_card(front=front_stub, back=back_stub)

        self.assertIsInstance(flip_card, FlipCard)
        self.assertIsInstance(flip_card.id_, FlipCardId)
        self.assertIsInstance(flip_card.front_id, FlipCardSideIdFront)
        self.assertEqual(flip_card.front.value, front_stub.value)
        self.assertIsInstance(flip_card.back_id, FlipCardSideIdBack)
        self.assertEqual(flip_card.back.value, back_stub.value)
        self.assertIsInstance(flip_card.front_state, CardSideState)
        self.assertIsInstance(flip_card.back_state, CardSideState)
