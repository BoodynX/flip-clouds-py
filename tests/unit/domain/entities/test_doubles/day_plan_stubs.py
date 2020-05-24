from abc import ABC

from src.domain.entities.day_plan import DayPlan
from tests.unit.domain.vos.test_doubles.day_plan_id_stub import DayPlanId_Stub
from tests.unit.domain.vos.test_doubles.day_stub import Day_Stub
from tests.unit.domain.vos.test_doubles.unique_flip_card_sides_container_stubs import \
    UniqueFlipCardSidesContainer_StubMixedSides, UniqueFlipCardSidesContainer_StubFrontSides, \
    UniqueFlipCardSidesContainer_StubBackSides


class DayPlan_StubAbstraction(DayPlan, ABC):
    def __new__(cls, *args, **kwargs):
        return DayPlan(
            id_=cls.id_,
            unique_flip_card_sides_container=cls._unique_flip_card_sides_container,
            day=cls.day
        )


class DayPlan_StubMixedSides(DayPlan_StubAbstraction):
    id_ = DayPlanId_Stub()
    _unique_flip_card_sides_container = UniqueFlipCardSidesContainer_StubMixedSides()
    day = Day_Stub()


class DayPlan_StubFrontSides(DayPlan_StubAbstraction):
    id_ = DayPlanId_Stub()
    _unique_flip_card_sides_container = UniqueFlipCardSidesContainer_StubFrontSides()
    day = Day_Stub()


class DayPlan_StubBackSides(DayPlan_StubAbstraction):
    id_ = DayPlanId_Stub()
    _unique_flip_card_sides_container = UniqueFlipCardSidesContainer_StubBackSides()
    day = Day_Stub()
