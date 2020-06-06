from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.flip_card_id import FlipCardId
from src.domain.vos.sentence import Sentence


class FlipCard(Entity):
    def __init__(self, id_: FlipCardId, front: Sentence, back: Sentence):
        self.id_ = id_
        self.front = front
        self.back = back
