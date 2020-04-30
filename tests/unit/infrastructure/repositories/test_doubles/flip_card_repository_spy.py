from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardStub


class FlipCardsRepositorySpy(FlipCardRepositoryInterface):
    def __init__(self):
        self.call_stack = []

    def save(self, flip_card: FlipCard):
        self.call_stack.append((self.save.__name__, flip_card))

    def draw_a_random_card(self) -> FlipCard:
        return FlipCardStub()