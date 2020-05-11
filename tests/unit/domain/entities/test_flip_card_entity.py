from unittest import TestCase
from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_side_id import FlipCardSideIdFront, FlipCardSideIdBack
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateStubNew, CardSideStateStubDrawn
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceFrontStub, SentenceBackStub


class TestFlipCardEntity(TestCase):
    def test_get_drawn_side_id__front_drawn__return_front_id(self):
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=SentenceFrontStub(),
            front_id=FlipCardSideIdFront(uuid4()),
            back=SentenceBackStub(),
            back_id=FlipCardSideIdBack(uuid4()),
            front_state=CardSideStateStubDrawn(),
            back_state=CardSideStateStubNew()
        )

        flip_card_side_id = flip_card.get_drawn_side_id()

        self.assertIsInstance(flip_card_side_id, FlipCardSideIdFront)

    def test_get_drawn_side_id__back_drawn__return_front_id(self):
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=SentenceFrontStub(),
            front_id=FlipCardSideIdFront(uuid4()),
            back=SentenceBackStub(),
            back_id=FlipCardSideIdBack(uuid4()),
            front_state=CardSideStateStubNew(),
            back_state=CardSideStateStubDrawn()
        )

        flip_card_side_id = flip_card.get_drawn_side_id()

        self.assertIsInstance(flip_card_side_id, FlipCardSideIdBack)

    def test_get_drawn_side_id__not_drawn__return_none(self):
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=SentenceFrontStub(),
            front_id=FlipCardSideIdFront(uuid4()),
            back=SentenceBackStub(),
            back_id=FlipCardSideIdBack(uuid4()),
            front_state=CardSideStateStubNew(),
            back_state=CardSideStateStubNew()
        )

        flip_card_side_id = flip_card.get_drawn_side_id()

        self.assertIsNone(flip_card_side_id)

    def test_get_opposite_side_id__submitted_side_id__return_opposite_side_id(self):
        side_id_front = FlipCardSideIdFront(uuid4())
        side_id_back = FlipCardSideIdBack(uuid4())
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=SentenceFrontStub(),
            front_id=side_id_front,
            back=SentenceBackStub(),
            back_id=side_id_back,
            front_state=CardSideStateStubNew(),
            back_state=CardSideStateStubNew()
        )

        fetched_back_side_id = flip_card.get_opposite_side_id_to(side_id_front)
        fetched_front_side_id = flip_card.get_opposite_side_id_to(side_id_back)

        self.assertIsInstance(fetched_back_side_id, FlipCardSideIdBack)
        self.assertIsInstance(fetched_front_side_id, FlipCardSideIdFront)
