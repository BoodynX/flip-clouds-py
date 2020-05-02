from datetime import datetime, timedelta
from unittest import TestCase

from src.domain.entities.day_plan import DayPlan
from src.domain.event_log import EventLog
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.services.day_planner import DayPlanner
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from tests.unit.application.factories.test_doubles.day_plan_factory_spy import DayPlanFactorySpy
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardNewStub
from tests.unit.domain.vos.test_doubles.day_plan_id_stub import DayPlanIdStub
from tests.unit.domain.vos.test_doubles.number_of_days_stub import NumberOfDaysStub
from tests.unit.infrastructure.repositories.test_doubles.day_plan_repository_spy import DayPlanRepositorySpy, \
    EmptyDayPlanRepositorySpy


class TestDayPlanner(TestCase):
    def setUp(self) -> None:
        self.factory = DayPlanFactorySpy
        self.flip_card = FlipCardNewStub()
        self.number_of_days = NumberOfDaysStub()
        self.event_log = EventLog()

    def test_add_first_flip_card_to_plan__x_number_of_days_from_today__flip_card_in_plan(self):
        empty_repository = EmptyDayPlanRepositorySpy()
        day_planner = DayPlanner(event_log=self.event_log, repository=empty_repository, factory=self.factory)

        day_planner.add_flip_card_to_day_plan(flip_card=self.flip_card, days=self.number_of_days)

        self._assert_saved_to_repository(empty_repository)
        self._assert_day_plan_factory_called()

    def test_add_another_flip_card_to_plan__x_number_of_days_from_today__flip_card_in_plan(self):
        repository = DayPlanRepositorySpy()
        day_planner = DayPlanner(event_log=self.event_log, repository=repository, factory=self.factory)

        day_planner.add_flip_card_to_day_plan(flip_card=self.flip_card, days=self.number_of_days)

        self._assert_saved_to_repository(repository)

    def _assert_day_plan_factory_called(self):
        self.assertEqual(DayPlanFactorySpy.call_stack[0][0], DayPlanFactoryInterface.create_day_plan.__name__)
        flip_card_ids = DayPlanFactorySpy.call_stack[0][1][0]
        self.assertIsInstance(flip_card_ids, set)
        self.assertSetEqual(flip_card_ids, {self.flip_card.id_})
        day = DayPlanFactorySpy.call_stack[0][1][1]
        self.assertIsInstance(day, Day)
        self._assert_day_is_number_of_days_greater_then_today(day, self.number_of_days)

    def _assert_saved_to_repository(self, empty_repository):
        self.assertEqual(empty_repository.call_stack[1][0], empty_repository.save.__name__)
        day_plan = empty_repository.call_stack[1][1]
        self.assertIsInstance(day_plan, DayPlan)
        self.assertSetEqual(day_plan.flip_card_ids, DayPlanFactorySpy.day_plan_stub.flip_card_ids)
        self.assertIsInstance(day_plan.id_, DayPlanId)
        self.assertEqual(day_plan.id_.value, DayPlanIdStub.value)

    def _assert_day_is_number_of_days_greater_then_today(self, day, days):
        return self.assertTrue(day.value.date() == (datetime.today() + timedelta(days=days.value)).date(),
                               'Day is NOT number_of_days greater then today!')
