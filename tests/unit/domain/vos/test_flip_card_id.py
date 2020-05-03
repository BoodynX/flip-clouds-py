from unittest import TestCase

from src.domain.vos.flip_card_id import FlipCardId


class TestFlipCardId(TestCase):
    invalid_id = 'invalid id'

    def test_invalid_id__raise_exception(self):
        self.assertRaises(FlipCardId.InvalidFlipCardId, FlipCardId, self.invalid_id)
