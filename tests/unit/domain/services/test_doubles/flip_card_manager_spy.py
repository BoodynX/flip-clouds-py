from src.domain.services.flip_card_manager import IFlipCardManager
from tests.utils import CallStack


class FlipCardManager_Spy(IFlipCardManager):
    def __init__(self):
        self.call_stack = CallStack()

    def create_card(self, **kwargs):
        self.call_stack.append(method=IFlipCardManager.create_card, params=kwargs)
