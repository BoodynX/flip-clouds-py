from enum import Enum

from src.domain.vos.abstractions.value_object import ValueObject


class CardSideState(ValueObject):

    def _validate_value(self, value: 'StateType'):
        if not isinstance(value, self.StateType):
            raise self.InvalidFlipCardStateType()

    class StateType(Enum):
        NEW = 'new'  # Card newly created, gets persisted
        DRAWN = 'drawn'  # Card drawn from plan or repo, the side marked as DRAWN is shown to the user
        PLANNED = 'planned'  # Card side was put in to a day plan
        ARCHIVED = 'archived'  # Card side to be archived or is already

    class InvalidFlipCardStateType(Exception):
        """pass"""
