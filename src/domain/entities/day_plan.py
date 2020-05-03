from typing import Set

from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from src.domain.vos.flip_card_side_id import FlipCardSideId


class DayPlan(Entity):
    def __init__(self, id_: DayPlanId, flip_card_side_ids: Set[FlipCardSideId], day: Day):
        self.id_ = id_
        self.flip_card_side_ids = flip_card_side_ids
        self.day = day
