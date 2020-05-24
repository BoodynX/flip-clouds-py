from datetime import datetime, timedelta
from unittest import TestCase

from src.domain.entities.day_plan import DayPlan
from src.domain.entities.flip_card_side import FlipCardSide
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.services.day_planner import DayPlanner
from src.domain.services.event_log.event_log import EventLog
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer
from tests.unit.application.factories.test_doubles.day_plan_factory_spy import DayPlanFactory_Spy
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_Stub
from tests.unit.domain.vos.test_doubles.day_plan_id_stub import DayPlanId_Stub
from tests.unit.domain.vos.test_doubles.number_of_days_stub import NumberOfDays_Stub
from tests.unit.infrastructure.repositories.test_doubles.day_plan_repository_spies import \
    DayPlanRepository_SpyEmpty, DayPlanRepository_SpyFrontSides, DayPlanRepository_SpyAbstraction


class TestDayPlanner(TestCase):
    def setUp(self) -> None:
        self.factory = DayPlanFactory_Spy.get_fresh_spy()
        self.flip_card = FlipCard_Stub()
        self.number_of_days = NumberOfDays_Stub()
        self.event_log = EventLog()

    def test_add_first_flip_card_side_to_plan__x_number_of_days_from_today__flip_card_side_in_plan(self):
        empty_repository = DayPlanRepository_SpyEmpty()
        day_planner = DayPlanner(event_log=self.event_log, repository=empty_repository, factory=self.factory)
        flip_card_front = self.flip_card.front

        day_planner.add_flip_card_side_id_to_day_plan(side=flip_card_front,
                                                      days=self.number_of_days)

        self._assert_day_plan_fetched_from_repository(repository=empty_repository)
        self._assert_day_plan_factory_called()
        self._assert_saved_to_repository(repository=empty_repository, flip_card_side=flip_card_front)

    def test_add_another_flip_card_side_id_to_plan__x_number_of_days_from_today__flip_card_side_in_plan(self):
        repository = DayPlanRepository_SpyFrontSides()
        day_planner = DayPlanner(event_log=self.event_log, repository=repository, factory=self.factory)
        flip_card_side = self.flip_card.back

        day_planner.add_flip_card_side_id_to_day_plan(side=flip_card_side,
                                                      days=self.number_of_days)

        self._assert_day_plan_fetched_from_repository(repository=repository)
        self._assert_saved_to_repository(repository=repository, flip_card_side=flip_card_side)
        self._assert_flip_card_side_id_was_added_to_day_plan(flip_card_side, repository)

    def _assert_flip_card_side_id_was_added_to_day_plan(self, flip_card_side_id, repository):
        day_plan: DayPlan = repository.call_stack[1][2]
        self.assertIn(flip_card_side_id, day_plan._unique_flip_card_sides_container.value)

    def _assert_day_plan_factory_called(self):
        self.assertEqual(DayPlanFactory_Spy.call_stack[0][0], DayPlanFactoryInterface.create_day_plan.__name__)
        unique_flip_card_sides_container = DayPlanFactory_Spy.call_stack[0][1][0]
        self.assertIsInstance(unique_flip_card_sides_container, UniqueFlipCardSidesContainer)
        self.assertSetEqual(unique_flip_card_sides_container.value, {self.flip_card.front})
        day = DayPlanFactory_Spy.call_stack[0][1][1]
        self.assertIsInstance(day, Day)
        self._assert_day_is_number_of_days_greater_then_today(day=day)

    def _assert_saved_to_repository(self, repository: DayPlanRepository_SpyAbstraction,
                                    flip_card_side: FlipCardSide):
        self.assertEqual(repository.call_stack[1][0], repository.purge_side_id_from_all_plans_and_save_plan.__name__)
        flip_card_side_submitted = repository.call_stack[1][1]
        day_plan = repository.call_stack[1][2]
        self.assertIsInstance(day_plan, DayPlan)
        self.assertIsInstance(day_plan.id_, DayPlanId)
        self.assertEqual(day_plan.id_.value, DayPlanId_Stub.value)
        self.assertIsInstance(flip_card_side, FlipCardSide)
        self.assertEqual(flip_card_side_submitted.id_.value, flip_card_side.id_.value)

    def _assert_day_plan_fetched_from_repository(self, repository: DayPlanRepository_SpyAbstraction):
        self.assertEqual(repository.call_stack[0][0], repository.get.__name__)
        day = repository.call_stack[0][1]
        self.assertIsInstance(day, Day)
        self._assert_day_is_number_of_days_greater_then_today(day=day)

    def _assert_day_is_number_of_days_greater_then_today(self, day):
        return self.assertTrue(
            day.value.date() == (datetime.today() + timedelta(days=self.number_of_days.value)).date(),
            'Day is NOT number_of_days greater then today!')
