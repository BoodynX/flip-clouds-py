from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.entities.flip_card_side import FlipCardSide
from tests.unit.domain.entities.test_doubles.flip_card_side_stubs import FlipCardSide_StubFront, \
    FlipCardSide_StubBack, FlipCardSide_StubFront_Two
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardId_Stub


class TestFlipCard(TestCase):
    def test_submit_same_side_to_back_and_front__raise_exception(self):
        self.assertRaises(FlipCard.FrontAndBackCantBeEqual,
                          FlipCard,
                          id_=FlipCardId_Stub(),
                          front=FlipCardSide_StubFront(),
                          back=FlipCardSide_StubFront())

    def test_get_opposite_side__submitted_side__return_opposite_side(self):
        front = FlipCardSide_StubFront()
        back = FlipCardSide_StubBack()
        flip_card = FlipCard(
            id_=FlipCardId_Stub(),
            front=front,
            back=back,
        )

        fetched_back_side = flip_card.get_opposite_side_to(side=front)
        fetched_front_side = flip_card.get_opposite_side_to(side=back)

        self.assertIsInstance(fetched_back_side, FlipCardSide)
        self.assertIsInstance(fetched_front_side, FlipCardSide)

    def test_get_opposite_side__invalid_input__raise_exception(self):
        flip_card = FlipCard(
            id_=FlipCardId_Stub(),
            front=FlipCardSide_StubFront(),
            back=FlipCardSide_StubBack(),
        )

        self.assertRaises(FlipCard.InvalidSideType,
                          flip_card.get_opposite_side_to, side='')
        self.assertRaises(FlipCard.CardSideDoesNotBelongToCard,
                          flip_card.get_opposite_side_to,
                          side=FlipCardSide_StubFront_Two())
