from uuid import uuid4

from src.domain.entities.day_plan import DayPlan
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from src.domain.vos.day_plan_set import DayPlanSet


class DayPlanFactory(DayPlanFactoryInterface):
    @classmethod
    def create_day_plan(cls, day_plan_set: DayPlanSet, day: Day) -> DayPlan:
        return DayPlan(
            id_=DayPlanId(uuid4()),
            day_plan_set=day_plan_set,
            day=day
        )
