from typing import Set

from src.domain.entities.day_plan import DayPlan
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.vos.day import Day
from src.domain.vos.flip_card_id import FlipCardId
from src.domain.vos.flip_card_side_id import FlipCardSideId
from tests.unit.domain.entities.test_doubles.day_plan_stub import DayPlanStub


class DayPlanFactorySpy(DayPlanFactoryInterface):
    call_stack = []
    day_plan_stub = DayPlanStub()

    @classmethod
    def create_day_plan(cls, flip_card_side_ids: Set[FlipCardSideId], day: Day) -> DayPlan:
        cls.call_stack.append((cls.create_day_plan.__name__, (flip_card_side_ids, day)))

        return cls.day_plan_stub

    @classmethod
    def get_fresh_spy(cls):
        cls.call_stack = []
        cls.flip_card_stub = DayPlanStub()
        return cls
