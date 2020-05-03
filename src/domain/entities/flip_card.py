from typing import Union
from uuid import UUID

from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.day import Day
from src.domain.vos.sentence import Sentence
from src.domain.vos.flip_card_id import FlipCardId


class FlipCard(Entity):
    def __init__(self,
                 id_: FlipCardId,
                 front_id: UUID,
                 front: Sentence,
                 back_id: UUID,
                 back: Sentence,
                 front_state: CardSideState,
                 back_state: CardSideState,
                 front_planned_day: Union[Day, None] = None,
                 back_planned_day: Union[Day, None] = None):
        self.id_ = id_
        self.front_id = front_id
        self.front = front
        self.back_id = back_id
        self.back = back
        self.front_state = front_state
        self.back_state = back_state
        self.front_planned_day = front_planned_day
        self.back_planned_day = back_planned_day
