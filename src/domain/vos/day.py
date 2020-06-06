from datetime import datetime

from src.domain.vos.abstractions.value_object import ValueObject


class Day(ValueObject):

    def _validate_value(self, value):
        if not isinstance(value, datetime):
            raise self.InvalidDayValue()

    class InvalidDayValue(Exception):
        """pass"""
