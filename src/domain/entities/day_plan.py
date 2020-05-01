from typing import Set

from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.flip_card_id import FlipCardId


class DayPlan(Entity):
    def __init__(self, flip_card_ids: Set[FlipCardId] = None):
        self.flip_card_ids = flip_card_ids
