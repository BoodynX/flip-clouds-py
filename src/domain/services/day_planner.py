from datetime import datetime, timedelta
from typing import Type

from src.domain.entities.day_plan import DayPlan
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.repositories.day_plan_repository_interface import DayPlanRepositoryInterface

from src.domain.entities.flip_card import FlipCard
from src.domain.services.event_log.event_log import EventLog
from src.domain.vos.day import Day
from src.domain.vos.number_of_days import NumberOfDays


class DayPlanner:
    def __init__(self, event_log: EventLog,
                 repository: DayPlanRepositoryInterface,
                 factory: Type[DayPlanFactoryInterface]):
        self.event_log = event_log
        self.repository = repository
        self.factory = factory

    def add_flip_card_to_day_plan(self, flip_card: FlipCard, days: NumberOfDays):
        # TODO add side parameter

        day = self._calculate_date_of_next_appearance(days_to_next_appearance=days)
        day_plan: DayPlan = self.repository.get(day=day)

        if not day_plan:
            # TODO if day plan not found create new
            pass
        else:
            # TODO if day plan found add to it
            pass

        # TODO persist plan

    @staticmethod
    def _calculate_date_of_next_appearance(days_to_next_appearance):
        return Day(datetime.today() + timedelta(days=days_to_next_appearance.value))
