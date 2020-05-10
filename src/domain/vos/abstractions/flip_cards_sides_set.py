from abc import abstractmethod
from typing import Set

from src.domain.vos.abstractions.value_object import ValueObject
from src.domain.vos.flip_card_side_id import FlipCardSideId


class FlipCardSidesSet(ValueObject):
    def _validate_value(self, value: Set[FlipCardSideId]):
        if not isinstance(value, set):
            raise self.InvalidNewFlipCardsBufferValueType()
        for side_id in value:
            if not isinstance(side_id, FlipCardSideId):
                self._raise_exception()

    @abstractmethod
    def _raise_exception(self):
        """pass"""

    class InvalidNewFlipCardsBufferValueType(Exception):
        """pass"""