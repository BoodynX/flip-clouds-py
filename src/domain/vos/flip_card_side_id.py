from src.domain.vos.abstractions.uuid_value_object import UuidValueObject


class FlipCardSideId(UuidValueObject):
    def _raise_exception(self):
        raise self.InvalidFlipCardSideId()

    class InvalidFlipCardSideId(UuidValueObject.InvalidUuid):
        """pass"""