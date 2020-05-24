from src.domain.entities.flip_card_side import FlipCardSide
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideId_StubFront, \
    FlipCardSideId_StubBack, FlipCardSideId_StubFront_Two
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubBackEnglish, Sentence_StubFrontPolish


class FlipCardSide_StubFront(FlipCardSide):
    id_ = FlipCardSideId_StubFront()
    sentence = Sentence_StubFrontPolish()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
        )


class FlipCardSide_StubBack(FlipCardSide):
    id_ = FlipCardSideId_StubBack()
    sentence = Sentence_StubBackEnglish()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
        )


class FlipCardSide_StubFront_Two(FlipCardSide):
    id_ = FlipCardSideId_StubFront_Two()
    sentence = Sentence_StubFrontPolish()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
        )
