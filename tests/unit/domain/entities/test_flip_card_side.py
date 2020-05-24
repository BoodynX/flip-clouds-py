from unittest import TestCase

from src.domain.entities.flip_card_side import FlipCardSide
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideId_StubFront
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubBackEnglish


class TestFlipCardSide(TestCase):
    def test_flip_card_side(self):
        flip_card_side = FlipCardSide(
            id_=FlipCardSideId_StubFront(),
            sentence=Sentence_StubBackEnglish(),
        )

        self.assertIsInstance(flip_card_side, FlipCardSide)
