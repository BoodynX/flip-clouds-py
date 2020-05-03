from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_side_id import FlipCardSideId
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateNewStub, CardSideStatePlannedStub
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceBackStub, SentenceFrontStub


class FlipCardNewStub(FlipCard):

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=FlipCardIdStub(),
            front=SentenceFrontStub(),
            front_id=FlipCardSideId(uuid4()),
            back=SentenceBackStub(),
            back_id=FlipCardSideId(uuid4()),
            front_state=CardSideStateNewStub(),
            back_state=CardSideStateNewStub()
        )


class FlipCardHalfPlannedStub(FlipCard):

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=FlipCardIdStub(),
            front=SentenceFrontStub(),
            front_id=FlipCardSideId(uuid4()),
            back=SentenceBackStub(),
            back_id=FlipCardSideId(uuid4()),
            front_state=CardSideStateNewStub(),
            back_state=CardSideStatePlannedStub()
        )

