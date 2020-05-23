from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.entities.test_doubles.flip_card_side_stubs import FlipCardSideStubNewPolish, \
    FlipCardSideStubNewEnglish, FlipCardSideStubPlannedPolish, FlipCardSideStubPlannedEnglish, \
    FlipCardSideStubDrawnPolish, FlipCardSideStubDrawnEnglish
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardIdStub


class FlipCardStubNew(FlipCard):
    id_ = FlipCardIdStub()
    _front = FlipCardSideStubNewPolish()
    _back = FlipCardSideStubNewEnglish()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )


class FlipCardStubFrontPlanned(FlipCard):
    id_ = FlipCardIdStub()
    _front = FlipCardSideStubPlannedPolish()
    _back = FlipCardSideStubNewEnglish()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )


class FlipCardStubBackPlanned(FlipCard):
    id_ = FlipCardIdStub()
    _front = FlipCardSideStubNewPolish()
    _back = FlipCardSideStubPlannedEnglish()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )


class FlipCardStubFrontDrawn(FlipCard):
    id_ = FlipCardIdStub()
    _front = FlipCardSideStubDrawnPolish()
    _back = FlipCardSideStubNewEnglish()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )


class FlipCardStubBackDrawn(FlipCard):
    id_ = FlipCardIdStub()
    _front = FlipCardSideStubNewPolish()
    _back = FlipCardSideStubDrawnEnglish()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )
