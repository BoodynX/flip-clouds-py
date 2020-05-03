from src.domain.entities.day_plan import DayPlan
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardNewStub
from tests.unit.domain.vos.test_doubles.day_plan_id_stub import DayPlanIdStub
from tests.unit.domain.vos.test_doubles.day_stub import DayStub


class DayPlanStub(DayPlan):
    id_ = DayPlanIdStub()
    flip_card_side_ids = {FlipCardNewStub().front_id, FlipCardNewStub().back_id, FlipCardNewStub().front_id}
    day = DayStub()

    def __init__(self):
        pass
