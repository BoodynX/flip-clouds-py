from src.domain.entities.day_plan import DayPlan
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub


class DayPlanStub(DayPlan):
    flip_card_ids = {FlipCardIdStub(), FlipCardIdStub(), FlipCardIdStub()}

    def __init__(self):
        """pass"""
