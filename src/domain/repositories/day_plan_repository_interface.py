from abc import ABC, abstractmethod

from src.domain.entities.day_plan import DayPlan
from src.domain.vos.day import Day


class IDayPlanRepository(ABC):

    @abstractmethod
    def get_by_day(self, day: Day) -> DayPlan:
        """pass"""

    @abstractmethod
    def save(self, day_plan: DayPlan):
        """pass"""
