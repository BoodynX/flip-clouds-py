from src.domain.vos.day_plan_set import DayPlanSet
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideIdFrontStub, \
    FlipCardSideIdBackStub


class DayPlanSetStub(DayPlanSet):
    def __init__(self):
        self.value: set = {FlipCardSideIdFrontStub(), FlipCardSideIdBackStub(), FlipCardSideIdFrontStub()}


class DayPlanSetFrontSidesStub(DayPlanSet):
    def __init__(self):
        self.value: set = {FlipCardSideIdFrontStub(), FlipCardSideIdFrontStub(), FlipCardSideIdFrontStub()}


class DayPlanSetBackSidesStub(DayPlanSet):
    def __init__(self):
        self.value: set = {FlipCardSideIdBackStub(), FlipCardSideIdBackStub(), FlipCardSideIdBackStub()}
