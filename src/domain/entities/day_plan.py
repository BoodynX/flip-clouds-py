from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from src.domain.vos.day_plan_set import DayPlanSet
from src.domain.vos.flip_card_side_id import FlipCardSideId


class DayPlan(Entity):
    def __init__(self, id_: DayPlanId, day_plan_set: DayPlanSet, day: Day):
        self.id_ = id_
        self.day_plan_set = day_plan_set
        self.day = day

    def add_to_day_plan(self, flip_card_side_id: FlipCardSideId):
        appended_day_plan_set: set = self.day_plan_set.value
        appended_day_plan_set.add(flip_card_side_id)
        self.day_plan_set = DayPlanSet(appended_day_plan_set)
