from datetime import datetime
from uuid import UUID

from src.domain.vos.sentence import Sentence


class FlipCard:
    def __init__(self, id_: UUID, front: Sentence, back: Sentence, last_shown: datetime):
        self.id_ = id_
        self.front = front
        self.back = back
        self.last_shown = last_shown
