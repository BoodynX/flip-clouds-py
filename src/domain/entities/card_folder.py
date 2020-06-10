from uuid import UUID

from src.domain.entities.abstractions.entity import Entity
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.side import Side


class CardFolder(Entity):
    def __init__(self, id_: UUID, flip_card: FlipCard, side: Side):
        self.id_ = id_
        self.card = flip_card
        self.side = side
