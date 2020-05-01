from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.vos.test_doubles.card_state_dummy import CardStateDummy
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_back_stub import SentenceBackStub
from tests.unit.domain.vos.test_doubles.sentence_front_stub import SentenceFrontStub


class FlipCardStub(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceFrontStub()
        self.back = SentenceBackStub()
        self.state = CardStateDummy()
