from abc import ABC


class ValueObject(ABC):
    def __eq__(self, other: 'ValueObject'):
        if isinstance(other, ValueObject):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __hash__(self):
        return hash(tuple(self.__dict__.items()))

    def _immutability_check(self, attribute: str):
        if hasattr(self, attribute):
            raise self.ImmutableException()

    def _validate_type(self, obj: object, cls: type):
        if not isinstance(obj, cls):
            raise self.InvalidValue()

    class InvalidValue(Exception):
        """pass"""

    class ImmutableException(Exception):
        """pass"""
