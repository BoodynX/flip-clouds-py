from datetime import datetime
from unittest import TestCase
from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from tests.test_doubles.domain.vos.sentence_back_stub import SentenceBackStub
from tests.test_doubles.domain.vos.sentence_front_stub import SentenceFrontStub


class TestFlipCard(TestCase):
    def test_flip_card_creation__return_flip_card(self):
        uuid_ = uuid4()
        front_stub = SentenceFrontStub()
        back_stub = SentenceBackStub()
        last_shown = datetime(2020, 1, 1)

        flip_card = FlipCard(id_=uuid_,
                             front=front_stub,
                             back=back_stub,
                             last_shown=last_shown)

        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(flip_card.front, front_stub)
        self.assertEqual(flip_card.back, back_stub)
        self.assertEqual(flip_card.id_, uuid_)
        self.assertEqual(flip_card.last_shown, last_shown)
