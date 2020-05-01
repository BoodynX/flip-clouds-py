from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.vos.test_doubles.card_state_dummy import CardStateDummy
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_back_stub import SentenceBackStub
from tests.unit.domain.vos.test_doubles.sentence_front_stub import SentenceFrontStub


class TestFlipCard(TestCase):
    def test_flip_card_creation__return_flip_card(self):
        flip_card_id = FlipCardIdStub()
        front = SentenceFrontStub()
        back = SentenceBackStub()
        status = CardStateDummy()

        flip_card = FlipCard(id_=flip_card_id,
                             front=front,
                             back=back,
                             state=status)

        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(flip_card.front, front)
        self.assertEqual(flip_card.back, back)
        self.assertEqual(flip_card.id_.value, flip_card_id.value)
        self.assertEqual(flip_card.state, status)
