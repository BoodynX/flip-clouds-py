from abc import ABC, abstractmethod

from src.domain.entities.day_plan import DayPlan
from src.domain.vos.day import Day


class DayPlanFactoryInterface(ABC):
    @classmethod
    @abstractmethod
    def create_day_plan(cls, plan_items_box, day: Day) -> DayPlan:
        """pass"""
        # TODO this is unfinished
