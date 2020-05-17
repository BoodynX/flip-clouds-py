from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.flip_card_side_id import FlipCardSideId
from src.domain.vos.sentence import Sentence


class FlipCardSide(Entity):
    def __init__(self, id_: FlipCardSideId, sentence: Sentence, state: CardSideState):
        self.id_ = id_
        self.sentence = sentence
        self.state = state