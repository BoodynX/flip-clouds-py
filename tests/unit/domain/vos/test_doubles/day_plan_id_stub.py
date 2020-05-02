from uuid import uuid4

from src.domain.vos.day_plan_id import DayPlanId


class DayPlanIdStub(DayPlanId):
    value = uuid4()

    def __init__(self):
        """pass"""