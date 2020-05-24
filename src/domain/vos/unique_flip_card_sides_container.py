from typing import Set

from src.domain.entities.flip_card_side import FlipCardSide
from src.domain.vos.abstractions.value_object import ValueObject


class UniqueFlipCardSidesContainer(ValueObject):
    def _validate_value(self, value: Set[FlipCardSide]):
        self._validate_type(value)
        self._validate_included_items_type(value)
        self._validate_items_uniqueness(value)

    def _validate_type(self, value):
        if not isinstance(value, set):
            raise self.InvalidUniqueFlipCardSidesContainerValueType()

    def _validate_included_items_type(self, value):
        for side in value:
            if not isinstance(side, FlipCardSide):
                raise self.InvalidFlipCardSide()

    def _validate_items_uniqueness(self, value: Set[FlipCardSide]):
        id_values = set()
        for side in value:
            id_values.add(side.id_.value)

        if len(id_values) != len(value):
            raise self.ValueDuplicationDetected

    class InvalidUniqueFlipCardSidesContainerValueType(Exception):
        """pass"""

    class InvalidFlipCardSide(Exception):
        """pass"""

    class ValueDuplicationDetected(Exception):
        """pass"""
