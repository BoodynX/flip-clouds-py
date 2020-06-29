from src.domain.vos.abstractions.uuid_value_object import UuidValueObject


class FlipCardId(UuidValueObject):
    def _raise_exception(self, value):
        raise self.InvalidFlipCardId(value)

    class InvalidFlipCardId(UuidValueObject.InvalidUuid):
        """pass"""
