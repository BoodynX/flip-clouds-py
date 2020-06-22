from unittest import TestCase

from src.domain.vos.side import Side


class TestSide(TestCase):
    invalid_value = 'invalid_value'

    def test_side_invalid_value__raises_exception(self):
        self.assertRaises(Side.InvalidSideType, Side, value=self.invalid_value)

    def test_side_front__return_side_with_front_value(self):
        side = Side(Side.Type.FRONT)

        self.assertEqual(side.value, Side.Type.FRONT)
