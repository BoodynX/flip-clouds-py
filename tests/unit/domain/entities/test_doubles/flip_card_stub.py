from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateNewStub, CardSideStatePlannedStub
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceBackStub, SentenceFrontStub


class FlipCardNewStub(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceFrontStub()
        self.back = SentenceBackStub()
        self.front_state = CardSideStateNewStub()
        self.back_state = CardSideStateNewStub()


class FlipCardHalfPlannedStub(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceFrontStub()
        self.back = SentenceBackStub()
        self.front_state = CardSideStateNewStub()
        self.back_state = CardSideStatePlannedStub()
