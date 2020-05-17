from abc import ABC, abstractmethod

from src.domain.entities.day_plan import DayPlan
from src.domain.vos.day import Day
from src.domain.vos.flip_card_side_id import FlipCardSideId


class DayPlanRepositoryInterface(ABC):
    @abstractmethod
    def purge_side_id_from_all_plans_and_save_plan(self, side_id_to_purge: FlipCardSideId, day_plan: DayPlan):
        """Remove side_id_to_purge from all existing plans / new cards box and save new plan.
        This is to ensure that a side is planned only once"""

    @abstractmethod
    def get(self, day: Day) -> DayPlan:
        """pass"""
