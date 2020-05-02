from abc import ABC, abstractmethod

from src.domain.entities.day_plan import DayPlan
from src.domain.vos.day import Day


class DayPlanRepositoryInterface(ABC):
    @abstractmethod
    def save(self, day_plan: DayPlan):
        """pass"""

    @abstractmethod
    def get(self, day: Day) -> DayPlan:
        """pass"""
