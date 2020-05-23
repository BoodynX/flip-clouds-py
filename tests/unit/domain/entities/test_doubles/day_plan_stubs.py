from abc import ABC

from src.domain.entities.day_plan import DayPlan
from tests.unit.domain.vos.test_doubles.day_plan_id_stub import DayPlanId_Stub
from tests.unit.domain.vos.test_doubles.day_plan_set_stubs import DayPlanSet_StubMixedSides, DayPlanSet_StubFrontSides, \
    DayPlanSet_StubBackSides
from tests.unit.domain.vos.test_doubles.day_stub import Day_Stub


class DayPlan_StubAbstraction(DayPlan, ABC):
    def __new__(cls, *args, **kwargs):
        return DayPlan(
            id_=cls.id_,
            day_plan_set=cls.day_plan_set,
            day=cls.day
        )


class DayPlan_StubMixedSides(DayPlan_StubAbstraction):
    id_ = DayPlanId_Stub()
    day_plan_set = DayPlanSet_StubMixedSides()
    day = Day_Stub()


class DayPlan_StubFrontSides(DayPlan_StubAbstraction):
    id_ = DayPlanId_Stub()
    day_plan_set = DayPlanSet_StubFrontSides()
    day = Day_Stub()


class DayPlan_StubBackSides(DayPlan_StubAbstraction):
    id_ = DayPlanId_Stub()
    day_plan_set = DayPlanSet_StubBackSides()
    day = Day_Stub()
