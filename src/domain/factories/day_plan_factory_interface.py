from abc import ABC, abstractmethod
from typing import Set

from src.domain.entities.day_plan import DayPlan
from src.domain.vos.day import Day
from src.domain.vos.flip_card_side_id import FlipCardSideId


class DayPlanFactoryInterface(ABC):
    @classmethod
    @abstractmethod
    def create_day_plan(cls, flip_card_side_ids: Set[FlipCardSideId], day: Day) -> DayPlan:
        """pass"""
