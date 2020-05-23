from typing import Set

from src.domain.vos.abstractions.value_object import ValueObject
from src.domain.vos.flip_card_side_id import FlipCardSideId


class UniqueFlipCardSidesContainer(ValueObject):
    def _validate_value(self, value: Set[FlipCardSideId]):
        self._validate_type(value)
        self._validate_included_items_type(value)
        self._validate_items_uniqueness(value)

    def _validate_items_uniqueness(self, value: set):
        id_values = set()
        for side in value:
            id_values.add(side.value)

        if len(id_values) != len(value):
            raise self.ValueDuplicationDetected

    def _validate_included_items_type(self, value):
        for side in value:
            if not isinstance(side, FlipCardSideId):
                raise self.InvalidFlipCardSideId()

    def _validate_type(self, value):
        if not isinstance(value, set):
            raise self.InvalidUniqueFlipCardSidesContainerValueType()

    class InvalidUniqueFlipCardSidesContainerValueType(Exception):
        """pass"""

    class InvalidFlipCardSideId(Exception):
        """pass"""

    class ValueDuplicationDetected(Exception):
        """pass"""
