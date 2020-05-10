from src.domain.entities.day_plan import DayPlan
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardNewStub
from tests.unit.domain.vos.test_doubles.day_plan_id_stub import DayPlanIdStub
from tests.unit.domain.vos.test_doubles.day_plan_set_stubs import DayPlanSetStub, DayPlanSetFrontSidesStub, \
    DayPlanSetBackSidesStub
from tests.unit.domain.vos.test_doubles.day_stub import DayStub


class DayPlanStub(DayPlan):
    id_ = DayPlanIdStub()
    day_plan_set = DayPlanSetStub()
    day = DayStub()

    def __init__(self):
        pass


class DayPlanFrontSidesStub(DayPlan):
    id_ = DayPlanIdStub()
    day_plan_set = DayPlanSetFrontSidesStub()
    day = DayStub()

    def __init__(self):
        pass


class DayPlanBackSidesStub(DayPlan):
    id_ = DayPlanIdStub()
    day_plan_set = DayPlanSetBackSidesStub()
    day = DayStub()

    def __init__(self):
        pass
