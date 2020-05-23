from abc import ABC, abstractmethod

from src.domain.entities.day_plan import DayPlan
from src.domain.vos.day import Day
from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer


class DayPlanFactoryInterface(ABC):
    @classmethod
    @abstractmethod
    def create_day_plan(cls, unique_flip_card_sides_container: UniqueFlipCardSidesContainer, day: Day) -> DayPlan:
        """pass"""
