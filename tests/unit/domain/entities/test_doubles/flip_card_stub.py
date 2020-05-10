from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_side_id import FlipCardSideIdFront, FlipCardSideIdBack
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateNewStub, CardSideStatePlannedStub, \
    CardSideStateDrawnStub
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceBackStub, SentenceFrontStub


class FlipCardNewStub(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceFrontStub()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceBackStub()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateNewStub()
        self.back_state = CardSideStateNewStub()

    def get_drawn_side_id(self):
        """pass"""


class FlipCardFrontPlannedStub(FlipCard):
    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceFrontStub()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceBackStub()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStatePlannedStub()
        self.back_state = CardSideStateNewStub()

    def get_drawn_side_id(self):
        """pass"""


class FlipCardBackPlannedStub(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceFrontStub()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceBackStub()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateNewStub()
        self.back_state = CardSideStatePlannedStub()

    def get_drawn_side_id(self):
        """pass"""


class FlipCardFrontDrawnStub(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceFrontStub()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceBackStub()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateDrawnStub()
        self.back_state = CardSideStateNewStub()

    def get_drawn_side_id(self):
        return self.front_id


class FlipCardBackDrawnStub(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceFrontStub()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceBackStub()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateNewStub()
        self.back_state = CardSideStateDrawnStub()

    def get_drawn_side_id(self):
        return self.back_id
