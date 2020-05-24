from abc import ABC, abstractmethod

from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.flip_card_side_id import FlipCardSideId
from src.domain.vos.primary_set import PrimarySet
from src.domain.vos.secondary_set import SecondarySet


class BoxInterface(Entity, ABC):
    @abstractmethod
    def add_to_primary(self, flip_card_side_id: FlipCardSideId):
        """pass"""

    @abstractmethod
    def add_to_secondary(self, flip_card_side_id: FlipCardSideId):
        """pass"""


class Box(BoxInterface):
    def __init__(self, primary_set: PrimarySet, secondary_set: SecondarySet):
        self._primary_set = primary_set
        self._secondary_set = secondary_set

    def add_to_primary(self, flip_card_side_id: FlipCardSideId):
        appended_primary_set: set = self._primary_set.value
        appended_primary_set.add(flip_card_side_id)
        self._primary_set = PrimarySet(appended_primary_set)

    def add_to_secondary(self, flip_card_side_id: FlipCardSideId):
        appended_secondary_set: set = self._secondary_set.value
        appended_secondary_set.add(flip_card_side_id)
        self._secondary_set = PrimarySet(appended_secondary_set)