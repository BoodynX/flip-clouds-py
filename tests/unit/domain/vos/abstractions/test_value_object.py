from unittest import TestCase

from src.domain.vos.abstractions.standard_value_object import StandardValueObject
from src.domain.vos.abstractions.value_object import ValueObject


class TestValueObject(TestCase):
    sample_value = 'sample value'
    other_sample_value = 'other sample value'
    invalid_value_stub = 'invalid value stub'

    @classmethod
    def setUpClass(cls) -> None:
        cls.vo = cls.StandardValueObjectImpl(cls.sample_value)

    def test_instance__on_request__return_instance(self):
        self.assertIsInstance(self.vo, StandardValueObject)

    def test_immutability_of_value__on_change_attempt__raise_exception(self):
        self.assertRaises(ValueObject.ImmutableException, self.vo.__setattr__, 'value', self.sample_value)

    def test_retrieving_value_parameter__on_request__return_value_parameter(self):
        self.assertEqual(self.sample_value, self.vo.value)

    def test_value_validation__invalid_value__raise_an_exception(self):
        self.assertRaises(self.ExampleValidationException,
                          self.ValueObjectValidateValueExceptionStub,
                          self.invalid_value_stub)

    def test_equality__equal_vo__return_true(self):
        other_vo = self.StandardValueObjectImpl(self.sample_value)
        self.assertTrue(self.vo == other_vo)

    def test_equality__other_vo__return_false(self):
        other_vo = self.StandardValueObjectImpl(self.other_sample_value)
        self.assertFalse(self.vo == other_vo)

    class StandardValueObjectImpl(StandardValueObject):
        def _validate_value(self, value):
            pass

    class ValueObjectValidateValueExceptionStub(StandardValueObject):
        def _validate_value(self, value):
            raise TestValueObject.ExampleValidationException()

    class ExampleValidationException(Exception):
        pass
