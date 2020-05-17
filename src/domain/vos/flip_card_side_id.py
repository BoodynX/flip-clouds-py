from abc import ABC, abstractmethod

from src.domain.vos.abstractions.uuid_value_object import UuidValueObject


class FlipCardSideId(UuidValueObject):
    def _raise_exception(self):
        self._raise_specific_flip_card_side_id_exception()

    def _raise_specific_flip_card_side_id_exception(self):
        raise self.InvalidFlipCardSideId()

    class InvalidFlipCardSideId(Exception):
        """pass"""


class FlipCardSideIdFront(FlipCardSideId):
    def _raise_specific_flip_card_side_id_exception(self):
        raise self.InvalidFlipCardSideIdFront()

    class InvalidFlipCardSideIdFront(Exception):
        """pass"""


class FlipCardSideIdBack(FlipCardSideId):
    def _raise_specific_flip_card_side_id_exception(self):
        raise self.InvalidFlipCardSideIdBack()

    class InvalidFlipCardSideIdBack(Exception):
        """pass"""
