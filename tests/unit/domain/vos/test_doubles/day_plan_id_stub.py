from uuid import uuid4

from src.domain.vos.day_plan_id import DayPlanId


class DayPlanId_Stub(DayPlanId):
    value = uuid4()

    def __init__(self):
        """pass"""
