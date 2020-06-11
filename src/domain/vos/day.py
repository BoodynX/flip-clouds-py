from datetime import datetime

from src.domain.vos.abstractions.standard_value_object import StandardValueObject


class Day(StandardValueObject):

    def _validate_value(self, value):
        if not isinstance(value, datetime):
            raise self.InvalidDayValue()

    class InvalidDayValue(StandardValueObject.InvalidValue):
        """pass"""
