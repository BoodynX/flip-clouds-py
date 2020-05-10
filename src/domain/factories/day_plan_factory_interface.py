from abc import ABC, abstractmethod

from src.domain.entities.day_plan import DayPlan
from src.domain.vos.day import Day
from src.domain.vos.day_plan_set import DayPlanSet


class DayPlanFactoryInterface(ABC):
    @classmethod
    @abstractmethod
    def create_day_plan(cls, day_plan_set: DayPlanSet, day: Day) -> DayPlan:
        """pass"""
