from src.domain.vos.abstractions.value_object import ValueObject


class NumberOfDays(ValueObject):
    def _validate_value(self, value: int):
        if isinstance(value, int) and 31 > value > 0:
            raise self.InvalidNumberOfDays()

    class InvalidNumberOfDays(Exception):
        """pass"""
