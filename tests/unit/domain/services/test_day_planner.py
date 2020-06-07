from datetime import datetime
from unittest import TestCase

from freezegun import freeze_time

from src.domain.repositories.day_plan_repository_interface import IDayPlanRepository
from src.domain.services.day_planner import DayPlanner
from src.domain.vos.day import Day
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_Stub
from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLog_Spy
from tests.unit.domain.vos.test_doubles.number_of_days_stub import NumberOfDays_Stub
from tests.unit.domain.vos.test_doubles.side_stubs import Side_Stub_Front
from tests.unit.infrastructure.repositories.test_doubles.day_plan_repository_spy import DayPlanRepository_Spy


class TestDayPlanner(TestCase):
    today_stub = datetime(2000, 1, 1)
    three_days_from_today_stub = datetime(2000, 1, 4)

    def setUp(self) -> None:
        self.flip_card = FlipCard_Stub()
        self.number_of_days = NumberOfDays_Stub()
        self.event_log = EventLog_Spy()
        self.day_plan_repository = DayPlanRepository_Spy()
        self.side = Side_Stub_Front()

    @freeze_time(today_stub)
    def test_calculate_date_of_next_appearance__return_day_x_number_of_days_in_the_future(self):
        days = NumberOfDays_Stub()

        day: Day = DayPlanner._calculate_date_of_next_appearance(days_to_next_appearance=days)

        self.assertEqual(day.value, self.three_days_from_today_stub)

    def test_add_first_flip_card_to_plan__x_number_of_days_from_today__item_in_new_plan(self):
        day_planner = DayPlanner(event_log=self.event_log,
                                 repository=self.day_plan_repository)

        day_planner.add_flip_card_to_day_plan(flip_card=self.flip_card,
                                              side=self.side,
                                              days=self.number_of_days)

        self._assert_day_plan_fetched_from_repository()
        self._assert_flip_card_added_to_plan()
        self._assert_saved_to_repository()

    def _assert_day_plan_fetched_from_repository(self):
        call = self.day_plan_repository.call_stack.call(number=1)

        self.assertEqual(call.method, IDayPlanRepository.get_by_day)
        self.assertIsInstance(call.params['day'], Day)

    def _assert_flip_card_added_to_plan(self):
        day_plan_spy = self.day_plan_repository.day_plan_mock
        day_plan_spy.assert_flip_card_added_to_plan(
            call_number=1,
            flip_card=self.flip_card,
            side=self.side
        )

    def _assert_saved_to_repository(self):
        call = self.day_plan_repository.call_stack.call(2)

        self.assertEqual(call.method, IDayPlanRepository.save)
        self.assertEqual(call.params['day_plan'], self.day_plan_repository.day_plan_mock)
