from datetime import datetime, timedelta
from typing import Type

from src.domain.services.event_log.event_log import EventLog
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.repositories.day_plan_repository_interface import DayPlanRepositoryInterface
from src.domain.vos.day import Day
from src.domain.vos.flip_card_side_id import FlipCardSideId
from src.domain.vos.number_of_days import NumberOfDays


class DayPlanner:
    def __init__(self, event_log: EventLog,
                 repository: DayPlanRepositoryInterface,
                 factory: Type[DayPlanFactoryInterface]):
        self.event_log = event_log
        self.repository = repository
        self.factory = factory

    def add_flip_card_side_id_to_day_plan(self, flip_card_side_id: FlipCardSideId, days: NumberOfDays):
        day = self._calculate_date_of_next_appearance(days_to_next_appearance=days)
        day_plan = self.repository.get(day=day)

        if not day_plan:
            day_plan = self.factory.create_day_plan(flip_card_side_ids={flip_card_side_id}, day=day)
        else:
            day_plan.flip_card_side_ids.add(flip_card_side_id)

        self.repository.save(day_plan=day_plan)

    @staticmethod
    def _calculate_date_of_next_appearance(days_to_next_appearance):
        return Day(datetime.today() + timedelta(days=days_to_next_appearance.value))
