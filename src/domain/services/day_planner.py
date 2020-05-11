from datetime import datetime, timedelta
from typing import Type

from src.domain.entities.day_plan import DayPlan
from src.domain.services.event_log.event_log import EventLog
from src.domain.factories.day_plan_factory_interface import DayPlanFactoryInterface
from src.domain.repositories.day_plan_repository_interface import DayPlanRepositoryInterface
from src.domain.vos.day import Day
from src.domain.vos.day_plan_set import DayPlanSet
from src.domain.vos.flip_card_side_id import FlipCardSideId
from src.domain.vos.number_of_days import NumberOfDays


class DayPlanner:
    def __init__(self, event_log: EventLog,
                 repository: DayPlanRepositoryInterface,
                 factory: Type[DayPlanFactoryInterface]):
        self.event_log = event_log
        self.repository = repository
        self.factory = factory

    def add_flip_card_side_id_to_day_plan(self, side_id: FlipCardSideId, days: NumberOfDays):
        day = self._calculate_date_of_next_appearance(days_to_next_appearance=days)
        day_plan: DayPlan = self.repository.get(day=day)

        if not day_plan:
            day_plan = self.factory.create_day_plan(day_plan_set=DayPlanSet({side_id}), day=day)
        else:
            day_plan.add_to_day_plan(side_id=side_id)

        self.repository.purge_side_id_from_all_plans_and_save_plan(side_id_to_purge=side_id, day_plan=day_plan)

    @staticmethod
    def _calculate_date_of_next_appearance(days_to_next_appearance):
        return Day(datetime.today() + timedelta(days=days_to_next_appearance.value))
