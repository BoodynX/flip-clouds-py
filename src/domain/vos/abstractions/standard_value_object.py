from abc import abstractmethod

from src.domain.vos.abstractions.value_object import ValueObject


class StandardValueObject(ValueObject):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._immutability_check('_value')
        self._validate_value(value)
        self._value = value

    @abstractmethod
    def _validate_value(self, value):
        """ Raise an exception here in case submitted value doesn't meet VOs requirements """

