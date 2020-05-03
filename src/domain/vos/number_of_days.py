from src.domain.vos.abstractions.value_object import ValueObject


class NumberOfDays(ValueObject):
    min = 1
    max = 30

    def _validate_value(self, value: int):
        if not isinstance(value, int):
            raise self.InvalidNumberOfDaysType()
        if not self.max >= value >= self.min:
            raise self.InvalidNumberOfDays()

    class InvalidNumberOfDays(Exception):
        """pass"""

    class InvalidNumberOfDaysType(Exception):
        """pass"""
