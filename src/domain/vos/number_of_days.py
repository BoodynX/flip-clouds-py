from src.domain.vos.abstractions.standard_value_object import StandardValueObject


class NumberOfDays(StandardValueObject):
    min = 1
    max = 30

    def _validate_value(self, value: int):
        if not isinstance(value, int):
            raise self.InvalidNumberOfDaysType(value)
        if not self.max >= value >= self.min:
            raise self.InvalidNumberOfDays(value)

    class InvalidNumberOfDays(StandardValueObject.InvalidValue):
        """pass"""

    class InvalidNumberOfDaysType(StandardValueObject.InvalidValue):
        """pass"""
