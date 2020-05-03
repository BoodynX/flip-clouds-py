from unittest import TestCase

from src.domain.vos.number_of_days import NumberOfDays


class TestNumberOfDays(TestCase):
    invalid_no_of_days_type = 'invalid no of days type'
    invalid_no_of_days = NumberOfDays.max + 1

    def test_invalid_number_of_days_type__raise_exception(self):
        self.assertRaises(NumberOfDays.InvalidNumberOfDaysType, NumberOfDays, self.invalid_no_of_days_type)

    def test_invalid_number_of_days__raise_exception(self):
        self.assertRaises(NumberOfDays.InvalidNumberOfDays, NumberOfDays, self.invalid_no_of_days)
