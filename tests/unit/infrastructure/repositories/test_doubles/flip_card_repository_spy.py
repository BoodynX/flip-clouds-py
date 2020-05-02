from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.flip_card_id import FlipCardId
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardStub


class FlipCardsRepositorySpy(FlipCardRepositoryInterface):
    def __init__(self):
        self.call_stack = []

    def save(self, flip_card: FlipCard):
        self.call_stack.append((self.save.__name__, flip_card))

    def draw_random_new_card(self) -> FlipCard:
        self.call_stack.append((self.draw_random_new_card.__name__,))
        return FlipCardStub()

    def get(self, id_: FlipCardId) -> FlipCard:
        self.call_stack.append((self.get.__name__, id_))
        return FlipCardStub()
