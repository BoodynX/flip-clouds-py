from unittest.case import TestCase

from src.application.factories.day_plan_factory import DayPlanFactory
from src.domain.entities.day_plan import DayPlan
from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer
from tests.unit.domain.vos.test_doubles.unique_flip_card_sides_container_stubs import \
    UniqueFlipCardSidesContainer_StubMixedSides
from tests.unit.domain.vos.test_doubles.day_stub import Day_Stub


class TestDayPlanFactory(TestCase):
    def test_day_plan_creation__return_day_plan(self):
        unique_flip_card_sides_container = UniqueFlipCardSidesContainer_StubMixedSides()
        day = Day_Stub()

        day_plan = DayPlanFactory.create_day_plan(day=day,
                                                  unique_flip_card_sides_container=unique_flip_card_sides_container)

        self.assertIsInstance(day_plan, DayPlan)
        self.assertIsInstance(day_plan._unique_flip_card_sides_container, UniqueFlipCardSidesContainer)
        self.assertSetEqual(day_plan._unique_flip_card_sides_container.value, unique_flip_card_sides_container.value)
        self.assertEqual(day, day_plan.day)
