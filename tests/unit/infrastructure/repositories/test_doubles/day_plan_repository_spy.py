from src.domain.entities.day_plan import IDayPlan
from tests.unit.domain.entities.test_doubles.day_plan_mock import DayPlan_Mock
from src.domain.repositories.day_plan_repository_interface import IDayPlanRepository
from tests.utils import CallStack


class DayPlanRepository_Spy(IDayPlanRepository):
    def __init__(self):
        self.call_stack = CallStack()
        self.day_plan_mock = DayPlan_Mock()

    def get_by_day(self, **kwargs) -> IDayPlan:
        self.call_stack.append(method=IDayPlanRepository.get_by_day, params=kwargs)
        return self.day_plan_mock

    def save(self, **kwargs):
        self.call_stack.append(method=IDayPlanRepository.save, params=kwargs)
