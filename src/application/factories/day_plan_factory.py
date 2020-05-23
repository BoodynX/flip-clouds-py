from uuid import uuid4

from src.domain.entities.day_plan import DayPlan
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer


class DayPlanFactory(DayPlanFactoryInterface):
    @classmethod
    def create_day_plan(cls, unique_flip_card_sides_container: UniqueFlipCardSidesContainer, day: Day) -> DayPlan:
        return DayPlan(
            id_=DayPlanId(uuid4()),
            unique_flip_card_sides_container=unique_flip_card_sides_container,
            day=day
        )
