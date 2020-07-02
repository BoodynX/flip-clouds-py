from datetime import datetime, timedelta

from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.i_day_plan_repository import IDayPlanRepository
from src.domain.services.event_log.event_log import EventLog
from src.domain.vos.day import Day
from src.domain.vos.number_of_days import NumberOfDays
from src.domain.vos.side import Side


class DayPlanner:
    def __init__(self, event_log: EventLog,
                 repository: IDayPlanRepository):
        self.event_log = event_log
        self.repository = repository

    def add_flip_card_to_day_plan(self, flip_card: FlipCard, side: Side, days: NumberOfDays):
        day = self._calculate_date_of_next_appearance(days_to_next_appearance=days)
        day_plan = self.repository.get_by_day(day=day)
        day_plan.add_flip_card(flip_card=flip_card, side=side)
        self.repository.save(day_plan=day_plan)

    @staticmethod
    def _calculate_date_of_next_appearance(days_to_next_appearance):
        return Day(datetime.today() + timedelta(days=days_to_next_appearance.value))
