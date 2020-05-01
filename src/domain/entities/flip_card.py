from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.card_state import CardState
from src.domain.vos.sentence import Sentence
from src.domain.vos.flip_card_id import FlipCardId


class FlipCard(Entity):
    def __init__(self, id_: FlipCardId, front: Sentence, back: Sentence, state: CardState):
        self.id_ = id_
        self.front = front
        self.back = back
        self.state = state
