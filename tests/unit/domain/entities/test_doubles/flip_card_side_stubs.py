from src.domain.entities.flip_card_side import FlipCardSide
from tests.unit.domain.vos.test_doubles.card_side_state_stub import CardSideStateStubDrawn, CardSideStateStubNew, \
    CardSideStateStubPlanned
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideIdStubPolish, \
    FlipCardSideIdStubEnglish
from tests.unit.domain.vos.test_doubles.sentence_stub import SentenceStubEnglish, SentenceStubPolish


class FlipCardSideStubNewPolish(FlipCardSide):
    id_ = FlipCardSideIdStubPolish()
    sentence = SentenceStubPolish()
    state = CardSideStateStubNew()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSideStubNewEnglish(FlipCardSide):
    id_ = FlipCardSideIdStubEnglish()
    sentence = SentenceStubEnglish()
    state = CardSideStateStubNew()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSideStubDrawnEnglish(FlipCardSide):
    id_ = FlipCardSideIdStubEnglish()
    sentence = SentenceStubEnglish()
    state = CardSideStateStubDrawn()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSideStubDrawnPolish(FlipCardSide):
    id_ = FlipCardSideIdStubPolish()
    sentence = SentenceStubPolish()
    state = CardSideStateStubDrawn()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSideStubPlannedPolish(FlipCardSide):
    id_ = FlipCardSideIdStubPolish()
    sentence = SentenceStubPolish()
    state = CardSideStateStubPlanned()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )


class FlipCardSideStubPlannedEnglish(FlipCardSide):
    id_ = FlipCardSideIdStubEnglish()
    sentence = SentenceStubEnglish()
    state = CardSideStateStubPlanned()

    def __new__(cls, *args, **kwargs):
        return FlipCardSide(
            id_=cls.id_,
            sentence=cls.sentence,
            state=cls.state
        )
