from unittest import TestCase

from src.domain.vos.card_set_count import CardSetCount


class TestCardSetCount(TestCase):
    def test_invalid_card_set_count__raise_exception(self):
        self.assertRaises(CardSetCount.InvalidCardSetCount, CardSetCount, CardSetCount.min_count - 1)
        self.assertRaises(CardSetCount.InvalidCardSetCount, CardSetCount, CardSetCount.max_count + 1)

    def test_valid_card_set_count__success(self):
        vo = CardSetCount(CardSetCount.min_count)

        self.assertEqual(vo.value, CardSetCount.min_count)
