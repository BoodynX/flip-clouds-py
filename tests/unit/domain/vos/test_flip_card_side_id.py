from unittest import TestCase

from src.domain.vos.flip_card_side_id import FlipCardSideIdFront, FlipCardSideIdBack


class TestFlipCardId(TestCase):
    invalid_id = 'invalid id'

    def test_invalid_front_id__raise_exception(self):
        self.assertRaises(FlipCardSideIdFront.InvalidFlipCardSideIdFront, FlipCardSideIdFront, self.invalid_id)

    def test_invalid_back_id__raise_exception(self):
        self.assertRaises(FlipCardSideIdBack.InvalidFlipCardSideIdBack, FlipCardSideIdBack, self.invalid_id)
