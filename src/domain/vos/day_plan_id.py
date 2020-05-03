from src.domain.vos.abstractions.uuid_value_object import UuidValueObject


class DayPlanId(UuidValueObject):
    def _raise_exception(self):
        raise self.InvalidDayPlanId()

    class InvalidDayPlanId(UuidValueObject.InvalidUuid):
        """pass"""
