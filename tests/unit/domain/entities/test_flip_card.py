from unittest import TestCase

from src.domain.entities.flip_card import FlipCard
from src.domain.entities.flip_card_side import FlipCardSide
from tests.unit.domain.entities.test_doubles.flip_card_side_stubs import FlipCardSideStubNewPolish, \
    FlipCardSideStubDrawnEnglish, FlipCardSideStubPlannedPolish
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub


class TestFlipCard(TestCase):
    def test_submit_same_side_to_back_and_front__raise_exception(self):
        self.assertRaises(FlipCard.FrontAndBackCantBeEqual,
                          FlipCard,
                          id_=FlipCardIdStub(),
                          front=FlipCardSideStubNewPolish(),
                          back=FlipCardSideStubNewPolish())

    def test_get_drawn_side__front_drawn__return_front(self):
        side_stub_drawn = FlipCardSideStubDrawnEnglish()
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=side_stub_drawn,
            back=FlipCardSideStubNewPolish(),
        )

        flip_card_side = flip_card.get_drawn_side()

        self.assertIsInstance(flip_card_side, FlipCardSide)
        self.assertEqual(flip_card_side, side_stub_drawn)

    def test_get_drawn_side__back_drawn__return_back(self):
        side_stub_drawn = FlipCardSideStubDrawnEnglish()
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=FlipCardSideStubNewPolish(),
            back=side_stub_drawn,
        )

        flip_card_side = flip_card.get_drawn_side()

        self.assertIsInstance(flip_card_side, FlipCardSide)
        self.assertEqual(flip_card_side, side_stub_drawn)

    def test_get_drawn_side_id__not_drawn__return_none(self):
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=FlipCardSideStubNewPolish(),
            back=FlipCardSideStubPlannedPolish(),
        )

        flip_card_side = flip_card.get_drawn_side()

        self.assertIsNone(flip_card_side)

    def test_get_opposite_side_id__submitted_side_id__return_opposite_side_id(self):
        front = FlipCardSideStubNewPolish()
        back = FlipCardSideStubDrawnEnglish()
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=front,
            back=back,
        )

        fetched_back_side = flip_card.get_opposite_side_to(side=front)
        fetched_front_side = flip_card.get_opposite_side_to(side=back)

        self.assertIsInstance(fetched_back_side, FlipCardSide)
        self.assertIsInstance(fetched_front_side, FlipCardSide)

    def test_get_opposite_side_id__invalid_input__raise_exception(self):
        flip_card = FlipCard(
            id_=FlipCardIdStub(),
            front=FlipCardSideStubNewPolish(),
            back=FlipCardSideStubDrawnEnglish(),
        )

        self.assertRaises(FlipCard.InvalidSideType,
                          flip_card.get_opposite_side_to, side='')
        self.assertRaises(FlipCard.CardSideDoesNotBelongToCard,
                          flip_card.get_opposite_side_to,
                          side=FlipCardSideStubPlannedPolish())
