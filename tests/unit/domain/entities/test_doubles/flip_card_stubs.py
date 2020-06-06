from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardId_Stub
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubFrontPolish, Sentence_StubBackEnglish


class FlipCard_Stub(FlipCard):
    id_ = FlipCardId_Stub()
    front = Sentence_StubFrontPolish()
    back = Sentence_StubBackEnglish()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls.front,
            back=cls.back,
        )
