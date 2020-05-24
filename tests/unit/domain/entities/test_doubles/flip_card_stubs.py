from src.domain.entities.flip_card import FlipCard
from tests.unit.domain.entities.test_doubles.flip_card_side_stubs import FlipCardSide_StubFront, \
    FlipCardSide_StubBack
from tests.unit.domain.vos.test_doubles.flip_card_id_stub import FlipCardId_Stub


class FlipCard_Stub(FlipCard):
    id_ = FlipCardId_Stub()
    front = FlipCardSide_StubFront()
    back = FlipCardSide_StubBack()

    def __new__(cls, *args, **kwargs):
        return FlipCard(
            id_=cls.id_,
            front=cls.front,
            back=cls.back,
        )
