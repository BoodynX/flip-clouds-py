from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_side_id import FlipCardSideIdFront, FlipCardSideIdBack
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateStubNew, CardSideStateStubPlanned, \
    CardSideStateStubDrawn
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceStubBack, SentenceStubFront


class FlipCardStubNew(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceStubFront()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceStubBack()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateStubNew()
        self.back_state = CardSideStateStubNew()

    def get_drawn_side_id(self):
        """pass"""


class FlipCardStubFrontPlanned(FlipCard):
    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceStubFront()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceStubBack()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateStubPlanned()
        self.back_state = CardSideStateStubNew()

    def get_drawn_side_id(self):
        """pass"""


class FlipCardStubBackPlanned(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceStubFront()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceStubBack()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateStubNew()
        self.back_state = CardSideStateStubPlanned()

    def get_drawn_side_id(self):
        """pass"""


class FlipCardStubFrontDrawn(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceStubFront()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceStubBack()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateStubDrawn()
        self.back_state = CardSideStateStubNew()

    def get_drawn_side_id(self):
        return self.front_id


class FlipCardStubBackDrawn(FlipCard):

    def __init__(self):
        self.id_ = FlipCardIdStub()
        self.front = SentenceStubFront()
        self.front_id = FlipCardSideIdFront(uuid4())
        self.back = SentenceStubBack()
        self.back_id = FlipCardSideIdBack(uuid4())
        self.front_state = CardSideStateStubNew()
        self.back_state = CardSideStateStubDrawn()

    def get_drawn_side_id(self):
        return self.back_id
