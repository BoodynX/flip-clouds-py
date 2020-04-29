from datetime import datetime
from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from tests.test_doubles.domain.vos.sentence_back_stub import SentenceBackStub
from tests.test_doubles.domain.vos.sentence_front_stub import SentenceFrontStub


class FlipCardStub(FlipCard):
    last_shown_stub = datetime(2020, 1, 1)

    def __init__(self):
        self.id_ = uuid4()
        self.front = SentenceFrontStub()
        self.back = SentenceBackStub()
        self.last_shown = self.last_shown_stub
