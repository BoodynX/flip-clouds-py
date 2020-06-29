from uuid import UUID

from src.domain.vos.sentence import Sentence


class NewFlipCardResponse:
    def __init__(self, id_: UUID, front: Sentence, back: Sentence):
        self.id_ = id_
        self.front = front
        self.back = back
