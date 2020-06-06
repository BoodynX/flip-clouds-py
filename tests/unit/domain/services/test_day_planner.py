from datetime import datetime, timedelta
from unittest import TestCase

from src.domain.services.event_log.event_log import EventLog
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_Stub
from tests.unit.domain.vos.test_doubles.number_of_days_stub import NumberOfDays_Stub


class TestDayPlanner(TestCase):
    def setUp(self) -> None:
        self.flip_card = FlipCard_Stub()
        self.number_of_days = NumberOfDays_Stub()
        self.event_log = EventLog()

    def test_add_first_flip_card_to_plan__x_number_of_days_from_today__item_in_plan(self):
        pass
        # TODO
        # day_planner.add_flip_card_to_day_plan()
        #
        # self._assert_day_plan_fetched_from_repository(repository=empty_repository)
        # self._assert_day_plan_factory_called()
        # self._assert_saved_to_repository(repository=empty_repository, flip_card_side=flip_card_front)

    def test_add_another_flip_card_side_id_to_plan__x_number_of_days_from_today__flip_card_side_in_plan(self):
        pass
        # TODO
        # day_planner.add_flip_card_to_day_plan()

        # self._assert_day_plan_fetched_from_repository(repository=repository)
        # self._assert_saved_to_repository(repository=repository, flip_card_side=flip_card_back)
        # self._assert_flip_card_side_id_was_added_to_day_plan(flip_card_back, repository)

    def _assert_flip_card_side_id_was_added_to_day_plan(self, flip_card_side_id, repository):
        pass

    def _assert_day_plan_factory_called(self):
        pass

    def _assert_saved_to_repository(self):
        pass

    def _assert_day_plan_fetched_from_repository(self):
        pass

    def _assert_day_is_number_of_days_greater_then_today(self, day):
        return self.assertTrue(
            day.value.date() == (datetime.today() + timedelta(days=self.number_of_days.value)).date(),
            'Day is NOT number_of_days greater then today!')
