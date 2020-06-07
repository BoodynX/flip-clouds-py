from abc import abstractmethod, ABC

from src.domain.entities.abstractions.entity import Entity
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.side import Side


class IDayPlan(Entity, ABC):
    @abstractmethod
    def add_flip_card(self, flip_card: FlipCard, side: Side):
        pass


class DayPlan(IDayPlan):
    def add_flip_card(self, flip_card: FlipCard, side: Side):
        pass
        # TODO Implement


