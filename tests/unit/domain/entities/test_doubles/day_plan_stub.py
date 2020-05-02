from src.domain.entities.day_plan import DayPlan
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardStub
from tests.unit.domain.vos.test_doubles.day_plan_id_stub import DayPlanIdStub
from tests.unit.domain.vos.test_doubles.day_stub import DayStub


class DayPlanStub(DayPlan):
    id_ = DayPlanIdStub()
    flip_card_ids = {FlipCardStub().id_, FlipCardStub().id_, FlipCardStub().id_}
    day = DayStub()

    def __init__(self):
        """pass"""
