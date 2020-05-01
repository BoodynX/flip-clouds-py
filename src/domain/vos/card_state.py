from enum import Enum

from src.domain.vos.abstractions.value_object import ValueObject


class CardState(ValueObject):

    def _validate_value(self, value: 'StateType'):
        if not isinstance(value, self.StateType):
            raise self.InvalidFlipCardStateType()

    class StateType(Enum):
        NEW = 'New'
        PLANNED = 'Planned'
        ARCHIVED = 'Archived'

    class InvalidFlipCardStateType(Exception):
        """pass"""
