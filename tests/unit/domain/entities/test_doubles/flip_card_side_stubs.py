from src.domain.entities.flip_card_side import FlipCardSide
from tests.unit.domain.vos.test_doubles.card_side_state_stubs import CardSideState_StubDrawn, CardSideState_StubNew, \
    CardSideState_StubPlanned
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideId_StubFront, \
    FlipCardSideId_StubBack
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubBackEnglish, Sentence_StubFrontPolish


class FlipCardSide_StubFrontNew(FlipCardSide):
    id_ = FlipCardSideId_StubFront()
    sentence = Sentence_StubFrontPolish()
    state = CardSideState_StubNew()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSide_StubBackNew(FlipCardSide):
    id_ = FlipCardSideId_StubBack()
    sentence = Sentence_StubBackEnglish()
    state = CardSideState_StubNew()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSide_StubBackDrawn(FlipCardSide):
    id_ = FlipCardSideId_StubBack()
    sentence = Sentence_StubBackEnglish()
    state = CardSideState_StubDrawn()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSide_StubFrontDrawn(FlipCardSide):
    id_ = FlipCardSideId_StubFront()
    sentence = Sentence_StubFrontPolish()
    state = CardSideState_StubDrawn()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSide_StubFrontPlanned(FlipCardSide):
    id_ = FlipCardSideId_StubFront()
    sentence = Sentence_StubFrontPolish()
    state = CardSideState_StubPlanned()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSide_StubBackPlanned(FlipCardSide):
    id_ = FlipCardSideId_StubBack()
    sentence = Sentence_StubBackEnglish()
    state = CardSideState_StubPlanned()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )
