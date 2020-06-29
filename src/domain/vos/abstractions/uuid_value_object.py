from abc import abstractmethod
from uuid import UUID

from src.domain.vos.abstractions.standard_value_object import StandardValueObject


class UuidValueObject(StandardValueObject):
    def _validate_value(self, value: UUID):
        if not isinstance(value, UUID):
            self._raise_exception(value)

    @abstractmethod
    def _raise_exception(self, value):
        """pass"""

    class InvalidUuid(StandardValueObject.InvalidValue):
        """pass"""
