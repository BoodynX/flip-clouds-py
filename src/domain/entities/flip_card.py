from typing import Union

from src.domain.entities.abstractions.entity import Entity
from src.domain.entities.flip_card_side import FlipCardSide
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.flip_card_id import FlipCardId


class FlipCard(Entity):
    def __init__(self,
                 id_: FlipCardId,
                 front: FlipCardSide,
                 back: FlipCardSide,
                 ):
        if front.id_ == back.id_:
            raise self.FrontAndBackCantBeEqual()
        self.id_ = id_
        self._front = front
        self._back = back

    @property
    def front_id(self):
        return self._front.id_

    @property
    def back_id(self):
        return self._back.id_

    def get_opposite_side_to(self, side: FlipCardSide) -> FlipCardSide:
        if not isinstance(side, FlipCardSide):
            raise self.InvalidSideType()

        if side.id_ == self._front.id_:
            return self._back

        if side.id_ == self._back.id_:
            return self._front

        raise self.CardSideDoesNotBelongToCard()

    class InvalidSideType(Exception):
        """pass"""

    class CardSideDoesNotBelongToCard(Exception):
        """pass"""

    class FrontAndBackCantBeEqual(Exception):
        """pass"""
