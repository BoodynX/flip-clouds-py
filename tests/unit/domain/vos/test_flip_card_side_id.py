from unittest import TestCase

from src.domain.vos.flip_card_side_id import FlipCardSideId


class TestFlipCardId(TestCase):
    invalid_id = 'invalid id'

    def test_invalid_id__raise_exception(self):
        self.assertRaises(FlipCardSideId.InvalidFlipCardSideId, FlipCardSideId, self.invalid_id)
