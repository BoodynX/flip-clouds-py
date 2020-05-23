from abc import ABC

from src.domain.vos.day_plan_set import DayPlanSet
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideId_StubFront, \
    FlipCardSideId_StubBack, FlipCardSideId_StubFront_Two


class DayPlanSet_StubAbstraction(DayPlanSet, ABC):
    def __init__(self):
        """pass"""


class DayPlanSet_StubMixedSides(DayPlanSet_StubAbstraction):
    value: set = {FlipCardSideId_StubFront(), FlipCardSideId_StubBack(), FlipCardSideId_StubFront_Two()}


class DayPlanSet_StubFrontSides(DayPlanSet_StubAbstraction):
    value: set = {FlipCardSideId_StubFront()}


class DayPlanSet_StubBackSides(DayPlanSet_StubAbstraction):
    value: set = {FlipCardSideId_StubBack()}
