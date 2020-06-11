from unittest import TestCase

from src.domain.vos.abstractions.value_object import ValueObject
from src.domain.vos.card_folder import CardFolder
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_Stub
from tests.unit.domain.vos.test_doubles.side_stubs import Side_Stub_Front


class TestCardFolder(TestCase):
    def setUp(self):
        self.card_folder = CardFolder(card=FlipCard_Stub(), side=Side_Stub_Front())

    def test_valid_values__return_object(self):
        self.assertIsInstance(self.card_folder, CardFolder)

    def test_invalid_card_type__raise_exception(self):
        self.assertRaises(ValueObject.InvalidValue, CardFolder, card='invalid card type', side=Side_Stub_Front())

    def test_invalid_side_type__raise_exception(self):
        self.assertRaises(ValueObject.InvalidValue, CardFolder, card=FlipCard_Stub(), side='invalid side type')

    def test_immutability__try_to_change_fields__raise_exception(self):
        self.assertRaises(ValueObject.ImmutableException, self.card_folder.__setattr__, 'card', 'anything')
        self.assertRaises(ValueObject.ImmutableException, self.card_folder.__setattr__, 'side', 'anything')
