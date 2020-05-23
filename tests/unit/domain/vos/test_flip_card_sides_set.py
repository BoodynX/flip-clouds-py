from unittest.case import TestCase

from src.domain.vos.abstractions.flip_cards_sides_set import FlipCardSidesSet


class TestFlipCardSidesSet(TestCase):
    def setUp(self) -> None:
        self.invalid_set_type = 'this should be a set()'
        self.invalid_set_content = set('this should be a child of FlipCardSidesSet')

    def test_invalid_set_type__raise_exception(self):
        self.assertRaises(self.FlipCardSidesSetExample.InvalidFlipCardSidesValueType,
                          self.FlipCardSidesSetExample,
                          self.invalid_set_type)

    def test_invalid_set_content__raise_exception(self):
        self.assertRaises(self.FlipCardSidesSetExample.FlipCardSidesSetExampleException,
                          self.FlipCardSidesSetExample,
                          self.invalid_set_content)

    class FlipCardSidesSetExample(FlipCardSidesSet):
        def _raise_exception(self):
            raise self.FlipCardSidesSetExampleException()

        class FlipCardSidesSetExampleException(FlipCardSidesSet.InvalidFlipCardSidesValueType):
            """pass"""
