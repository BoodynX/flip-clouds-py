from datetime import datetime
from unittest.case import TestCase

from src.domain.vos.day import Day


class TestDay(TestCase):
    invalid_day_value = 'invalid day value'

    def test_invalid_day_value__raise_exception(self):
        self.assertRaises(Day.InvalidDayValue, Day, self.invalid_day_value)

    def test_valid_day_value__return_instance(self):
        datetime_obj = datetime(2020, 1, 1)

        day = Day(datetime_obj)

        self.assertEqual(datetime_obj, day.value)