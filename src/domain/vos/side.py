from enum import Enum

from src.domain.vos.abstractions.standard_value_object import StandardValueObject
from src.domain.vos.abstractions.value_object import ValueObject


class Side(StandardValueObject):
    @classmethod
    def front(cls):
        # TODO test this
        return cls(cls.Type.FRONT)

    @classmethod
    def back(cls):
        # TODO test this
        return cls(cls.Type.BACK)

    def _validate_value(self, value: 'Type'):
        if not isinstance(value, self.Type):
            raise self.InvalidSideType()

    class Type(Enum):
        FRONT = 'front'
        BACK = 'back'

    class InvalidSideType(ValueObject.InvalidValue):
        """pass"""
