from unittest.case import TestCase

from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer
from tests.unit.domain.entities.test_doubles.flip_card_side_stubs import FlipCardSide_StubFront


class TestUniqueFlipCardSidesContainer(TestCase):
    def setUp(self) -> None:
        self.invalid_set_type = 'this should be a set()'
        self.invalid_set_content = {'this should be a child of UniqueFlipCardSidesContainer'}
        self.set_with_duplicates = {FlipCardSide_StubFront(), FlipCardSide_StubFront()}

    def test_invalid_value_type__raise_exception(self):
        self.assertRaises(UniqueFlipCardSidesContainer.InvalidUniqueFlipCardSidesContainerValueType,
                          UniqueFlipCardSidesContainer,
                          self.invalid_set_type)

    def test_invalid_included_items__raise_exception(self):
        self.assertRaises(UniqueFlipCardSidesContainer.InvalidFlipCardSide,
                          UniqueFlipCardSidesContainer,
                          self.invalid_set_content)

    def test_duplicated_items_values__raise_exception(self):
        self.assertRaises(UniqueFlipCardSidesContainer.ValueDuplicationDetected,
                          UniqueFlipCardSidesContainer,
                          self.set_with_duplicates)
