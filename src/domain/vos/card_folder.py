from src.domain.entities.flip_card import FlipCard
from src.domain.vos.abstractions.value_object import ValueObject
from src.domain.vos.side import Side


class CardFolder(ValueObject):
    def __init__(self, card: FlipCard, side: Side):
        self.card = card
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side: Side):
        self._immutability_check('_side')
        self._validate_type(side, Side)
        self._side = side

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, card: FlipCard):
        self._immutability_check('_card')
        self._validate_type(obj=card, cls=FlipCard)
        self._card = card
