from typing import Set

from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from src.domain.vos.flip_card_id import FlipCardId


class DayPlan(Entity):
    def __init__(self, id_: DayPlanId, flip_card_ids: Set[FlipCardId], day: Day):
        # TODO store side ids instead of flip card ids
        self.id_ = id_
        self.flip_card_ids = flip_card_ids
        self.day = day
