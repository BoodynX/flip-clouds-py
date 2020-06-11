from src.domain.vos.card_folder import CardFolder
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_Stub
from tests.unit.domain.vos.test_doubles.side_stubs import Side_Stub_Front


class CardFolder_Stub(CardFolder):
    flip_card = FlipCard_Stub()
    side = Side_Stub_Front()

    def __new__(cls, *args, **kwargs):
        return CardFolder(
            card=cls.flip_card,
            side=cls.side,
        )
