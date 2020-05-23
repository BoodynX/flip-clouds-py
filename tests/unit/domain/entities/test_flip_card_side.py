from unittest import TestCase

from src.domain.entities.flip_card_side import FlipCardSide
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateStubNew
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideIdStub
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceStubEnglish


class TestFlipCardSide(TestCase):
    def test_flip_card_side(self):
        flip_card_side = FlipCardSide(
            id_=FlipCardSideIdStub(),
            sentence=SentenceStubEnglish(),
            state=CardSideStateStubNew(),
        )

        self.assertIsInstance(flip_card_side, FlipCardSide)
