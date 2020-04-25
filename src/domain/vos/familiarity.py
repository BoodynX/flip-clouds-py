from enum import Enum

from src.domain.vos.abstractions.value_object import ValueObject


class Familiarity(ValueObject):

    def _validate_value(self, value: 'Level'):
        if not isinstance(value, self.Level):
            raise self.InvalidFamiliarityLevel

    class Level(Enum):
        NONE = 'none'
        LOW = 'low'
        MEDIUM = 'medium'
        PERFECT = 'perfect'

    class InvalidFamiliarityLevel(Exception):
        pass
