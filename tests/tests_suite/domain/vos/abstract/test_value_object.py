from unittest import TestCase

from src.domain.exceptions import ImmutableException
from src.domain.vos.abstractions.value_object import ValueObject


class TestValueObject(TestCase):
    def test_instance(self):
        vo = ValueObjectDummy(None)
        self.assertIsInstance(vo, ValueObject)

    def test_immutability_of_value__raise_exception(self):
        vo = ValueObjectDummy(None)
        self.assertRaises(ImmutableException, vo.__setattr__, 'value', None)


class ValueObjectDummy(ValueObject):
    def validate_value(self, value):
        pass
