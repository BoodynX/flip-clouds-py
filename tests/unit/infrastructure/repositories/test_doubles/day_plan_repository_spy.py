from typing import Union

from src.domain.entities.day_plan import DayPlan
from src.domain.repositories.day_plan_repository_interface import DayPlanRepositoryInterface
from src.domain.vos.day import Day
from src.domain.vos.flip_card_side_id import FlipCardSideId
from tests.unit.domain.entities.test_doubles.day_plan_stub import DayPlanStub


class DayPlanRepositorySpy(DayPlanRepositoryInterface):
    def __init__(self):
        self.call_stack = []

    def purge_side_id_from_all_plans_and_save_plan(self, side_id_to_purge: FlipCardSideId, day_plan: DayPlan):
        self.call_stack.append((self.purge_side_id_from_all_plans_and_save_plan.__name__, side_id_to_purge, day_plan))

    def get(self, day: Day) -> DayPlan:
        self.call_stack.append((self.get.__name__, day))
        return DayPlanStub()


class EmptyDayPlanRepositorySpy(DayPlanRepositorySpy):
    def get(self, day: Day) -> Union[DayPlan, None]:
        self.call_stack.append((self.get.__name__, day))
        return None
