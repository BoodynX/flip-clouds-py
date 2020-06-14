from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.flip_card_repository_interface import IFlipCardRepository
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_Stub


class FlipCardRepository_Spy(IFlipCardRepository):

    def __init__(self):
        self.call_stack = []
        self.flip_card = FlipCard_Stub()

    def save(self, flip_card: FlipCard):
        self.call_stack.append((self.save.__name__, flip_card))

    def get_new(self):
        self.call_stack.append((self.save.__name__,))
        return self.flip_card
