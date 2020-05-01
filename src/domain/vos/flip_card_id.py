from uuid import UUID

from src.domain.vos.abstractions.value_object import ValueObject


class FlipCardId(ValueObject):
    def _validate_value(self, value: UUID):
        if isinstance(value, UUID):
            raise self.InvalidFlipCardId()

    class InvalidFlipCardId(Exception):
        """pass"""