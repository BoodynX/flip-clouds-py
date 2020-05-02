from unittest.case import TestCase
from uuid import uuid4

from src.domain.vos.day_plan_id import DayPlanId


class TestDayPlanId(TestCase):
    invalid_id = 'invalid id'
    valid_id = uuid4()

    def test_invalid_day_plan_id__raise_exception(self):
        self.assertRaises(DayPlanId.InvalidDayPlanId, DayPlanId, self.invalid_id)

    def test_valid_day_plan_id__return_exception(self):
        day_plan_id = DayPlanId(self.valid_id)

        self.assertEqual(day_plan_id.value, self.valid_id)