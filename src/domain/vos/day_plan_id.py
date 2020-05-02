from uuid import UUID

from src.domain.vos.abstractions.value_object import ValueObject


class DayPlanId(ValueObject):
    def _validate_value(self, value: UUID):
        if not isinstance(value, UUID):
            raise self.InvalidDayPlanId()

    class InvalidDayPlanId(Exception):
        """pass"""