from typing import Set
from uuid import uuid4

from src.domain.entities.day_plan import DayPlan
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from src.domain.vos.flip_card_side_id import FlipCardSideId


class DayPlanFactory(DayPlanFactoryInterface):
    @classmethod
    def create_day_plan(cls, flip_card_side_ids: Set[FlipCardSideId], day: Day) -> DayPlan:
        return DayPlan(
            id_=DayPlanId(uuid4()),
            flip_card_side_ids=flip_card_side_ids,
            day=day
        )