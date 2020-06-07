from abc import ABC, abstractmethod

from src.domain.exceptions import ImmutableException


class ValueObject(ABC):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if hasattr(self, '_value'):
            raise ImmutableException('Value objects are immutable!')
        self._validate_value(value)
        self._value = value

    @abstractmethod
    def _validate_value(self, value):
        """ Raise an exception here in case submitted value doesn't meet VOs requirements """

    def equals(self, other: 'ValueObject'):
        return self.value == other.value

    class InvalidValue(Exception):
        """pass"""
