from src.domain.entities.day_plan import DayPlan
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.vos.day import Day
from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer
from tests.unit.domain.entities.test_doubles.day_plan_stubs import DayPlan_StubMixedSides


class DayPlanFactory_Spy(DayPlanFactoryInterface):
    call_stack = []
    day_plan_stub = DayPlan_StubMixedSides()

    @classmethod
    def create_day_plan(cls, unique_flip_card_sides_container: UniqueFlipCardSidesContainer, day: Day) -> DayPlan:
        cls.call_stack.append((cls.create_day_plan.__name__, (unique_flip_card_sides_container, day)))

        return cls.day_plan_stub

    @classmethod
    def get_fresh_spy(cls):
        cls.call_stack = []
        cls.flip_card_stub = DayPlan_StubMixedSides()
        return cls
