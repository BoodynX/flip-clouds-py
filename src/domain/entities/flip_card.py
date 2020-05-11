from typing import Union

from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.flip_card_id import FlipCardId
from src.domain.vos.flip_card_side_id import FlipCardSideIdFront, FlipCardSideIdBack, FlipCardSideId
from src.domain.vos.sentence import Sentence


class FlipCard(Entity):
    def __init__(self,
                 id_: FlipCardId,
                 front_id: FlipCardSideIdFront,
                 front: Sentence,
                 back_id: FlipCardSideIdBack,
                 back: Sentence,
                 front_state: CardSideState,
                 back_state: CardSideState):
        self.id_ = id_
        self.front_id = front_id
        self.front = front
        self.back_id = back_id
        self.back = back
        self.front_state = front_state
        self.back_state = back_state

    def get_drawn_side_id(self) -> Union[FlipCardSideId, None]:
        if self.front_state.value == CardSideState.StateType.DRAWN:
            return self.front_id
        if self.back_state.value == CardSideState.StateType.DRAWN:
            return self.back_id
        return None

    def get_opposite_side_id_to(self, side_id: FlipCardSideId) -> FlipCardSideId:
        if isinstance(side_id, FlipCardSideIdFront):
            return self.back_id
        if isinstance(side_id, FlipCardSideIdBack):
            return self.front_id
        raise self.InvalidIdType()

    class InvalidIdType(Exception):
        """pass"""
