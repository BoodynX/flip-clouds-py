from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateNewStub, CardSideStatePlannedStub
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceBackStub, SentenceFrontStub


class FlipCardNewStub(FlipCard):

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=FlipCardIdStub(),
            front=SentenceFrontStub(),
            back=SentenceBackStub(),
            front_state=CardSideStateNewStub(),
            back_state=CardSideStateNewStub()
        )


class FlipCardHalfPlannedStub(FlipCard):

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=FlipCardIdStub(),
            front=SentenceFrontStub(),
            back=SentenceBackStub(),
            front_state=CardSideStateNewStub(),
            back_state=CardSideStatePlannedStub()
        )

