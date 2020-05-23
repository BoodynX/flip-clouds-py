from unittest.case import TestCase

from src.application.factories.day_plan_factory import DayPlanFactory
from src.domain.entities.day_plan import DayPlan
from src.domain.vos.day_plan_set import DayPlanSet
from tests.unit.domain.vos.test_doubles.day_plan_set_stubs import DayPlanSet_StubMixedSides
from tests.unit.domain.vos.test_doubles.day_stub import Day_Stub


class TestDayPlanFactory(TestCase):
    def test_day_plan_creation__return_day_plan(self):
        day_plan_set = DayPlanSet_StubMixedSides()
        day = Day_Stub()

        day_plan = DayPlanFactory.create_day_plan(day=day, day_plan_set=day_plan_set)

        self.assertIsInstance(day_plan, DayPlan)
        self.assertIsInstance(day_plan.day_plan_set, DayPlanSet)
        self.assertSetEqual(day_plan.day_plan_set.value, day_plan_set.value)
        self.assertEqual(day, day_plan.day)
