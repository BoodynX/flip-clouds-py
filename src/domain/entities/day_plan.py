from random import choice

from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.day import Day
from src.domain.vos.day_plan_id import DayPlanId
from src.domain.vos.flip_card_side_id import FlipCardSideId
from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer


class DayPlan(Entity):
    def __init__(self, id_: DayPlanId, unique_flip_card_sides_container: UniqueFlipCardSidesContainer, day: Day):
        self.id_ = id_
        self._unique_flip_card_sides_container = unique_flip_card_sides_container
        self.day = day

    def add_to_day_plan(self, side: FlipCardSideId):
        sides_set: set = self._unique_flip_card_sides_container.value
        sides_set.add(side)
        self._unique_flip_card_sides_container = UniqueFlipCardSidesContainer(sides_set)

    def pick_random_flip_card_side_id(self):
        return choice(tuple(self._unique_flip_card_sides_container.value))

