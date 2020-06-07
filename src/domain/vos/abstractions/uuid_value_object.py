from abc import abstractmethod
from uuid import UUID

from src.domain.vos.abstractions.value_object import ValueObject


class UuidValueObject(ValueObject):
    def _validate_value(self, value: UUID):
        if not isinstance(value, UUID):
            self._raise_exception()

    @abstractmethod
    def _raise_exception(self):
        """pass"""

    class InvalidUuid(ValueObject.InvalidValue):
        """pass"""
