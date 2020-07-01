from src.domain.entities.flip_card import FlipCard
from src.domain.services.flip_card_manager import IFlipCardManager
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_Stub
from tests.framework.utils import CallStack


class FlipCardManager_Spy(IFlipCardManager):
    def __init__(self):
        self.call_stack = CallStack()

    def create_card(self, **kwargs) -> FlipCard:
        self.call_stack.append(method=IFlipCardManager.create_card, params=kwargs)

        return FlipCard_Stub()
