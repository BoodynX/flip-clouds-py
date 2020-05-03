from unittest.case import TestCase

from src.application.factories.day_plan_factory import DayPlanFactory
from src.domain.entities.day_plan import DayPlan
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardNewStub
from tests.unit.domain.vos.test_doubles.day_stub import DayStub


class TestDayPlanFactory(TestCase):
    def test_day_plan_creation__return_day_plan(self):
        flip_card_side_ids = {FlipCardNewStub().front_id, FlipCardNewStub().back_id}
        day = DayStub()

        day_plan = DayPlanFactory.create_day_plan(day=day, flip_card_side_ids=flip_card_side_ids)

        self.assertIsInstance(day_plan, DayPlan)
        self.assertSetEqual(day_plan.flip_card_side_ids, flip_card_side_ids)
        self.assertEqual(day, day_plan.day)