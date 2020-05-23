from unittest.case import TestCase

from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer


class TestUniqueFlipCardSidesContainer(TestCase):
    def setUp(self) -> None:
        self.invalid_set_type = 'this should be a set()'
        self.invalid_set_content = set('this should be a child of UniqueFlipCardSidesContainer')

    def test_invalid_set_type__raise_exception(self):
        self.assertRaises(UniqueFlipCardSidesContainer.InvalidUniqueFlipCardSidesContainerValueType,
                          UniqueFlipCardSidesContainer,
                          self.invalid_set_type)

    def test_invalid_set_content__raise_exception(self):
        self.assertRaises(UniqueFlipCardSidesContainer.InvalidFlipCardSideId,
                          UniqueFlipCardSidesContainer,
                          self.invalid_set_content)

