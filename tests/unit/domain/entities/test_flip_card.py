from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateNewStub
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceBackStub, SentenceFrontStub


class TestFlipCard(TestCase):
    def test_flip_card_creation__return_flip_card(self):
        flip_card_id = FlipCardIdStub()
        front = SentenceFrontStub()
        back = SentenceBackStub()
        status = CardSideStateNewStub()

        flip_card = FlipCard(id_=flip_card_id,
                             front=front,
                             back=back,
                             front_state=status,
                             back_state=status
                             )

        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(flip_card.front, front)
        self.assertEqual(flip_card.back, back)
        self.assertEqual(flip_card.id_.value, flip_card_id.value)
        self.assertEqual(flip_card.front_state, status)
        self.assertEqual(flip_card.back_state, status)
