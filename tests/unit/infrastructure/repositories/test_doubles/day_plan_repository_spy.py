from typing import Union

from src.domain.entities.day_plan import DayPlan
from src.domain.repositories.day_plan_repository_interface import DayPlanRepositoryInterface
from src.domain.vos.day import Day
from tests.unit.domain.entities.test_doubles.day_plan_stub import DayPlanStub


class DayPlanRepositorySpy(DayPlanRepositoryInterface):
    def __init__(self):
        self.call_stack = []

    def save(self, day_plan: DayPlan):
        self.call_stack.append((self.save.__name__, day_plan))

    def get(self, day: Day) -> DayPlan:
        self.call_stack.append((self.get.__name__, day))
        return DayPlanStub()


class EmptyDayPlanRepositorySpy(DayPlanRepositorySpy):
    def get(self, day: Day) -> Union[DayPlan, None]:
        self.call_stack.append((self.get.__name__, day))
        return None
