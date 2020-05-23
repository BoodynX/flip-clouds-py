from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.entities.test_doubles.flip_card_side_stubs import FlipCardSide_StubFrontNew, \
    FlipCardSide_StubBackNew, FlipCardSide_StubFrontPlanned, FlipCardSide_StubBackPlanned, \
    FlipCardSide_StubFrontDrawn, FlipCardSide_StubBackDrawn
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardId_Stub


class FlipCard_StubAllNew(FlipCard):
    id_ = FlipCardId_Stub()
    _front = FlipCardSide_StubFrontNew()
    _back = FlipCardSide_StubBackNew()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )


class FlipCard_StubFrontPlannedBackNew(FlipCard):
    id_ = FlipCardId_Stub()
    _front = FlipCardSide_StubFrontPlanned()
    _back = FlipCardSide_StubBackNew()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )


class FlipCard_StubFrontNewBackPlanned(FlipCard):
    id_ = FlipCardId_Stub()
    _front = FlipCardSide_StubFrontNew()
    _back = FlipCardSide_StubBackPlanned()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )


class FlipCard_StubFrontDrawnBackNew(FlipCard):
    id_ = FlipCardId_Stub()
    _front = FlipCardSide_StubFrontDrawn()
    _back = FlipCardSide_StubBackNew()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )


class FlipCard_StubFrontNewBackDrawn(FlipCard):
    id_ = FlipCardId_Stub()
    _front = FlipCardSide_StubFrontNew()
    _back = FlipCardSide_StubBackDrawn()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls._front,
            back=cls._back,
        )
