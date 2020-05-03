from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.flip_card_side_id import FlipCardSideId
from tests.unit.domain.entities.test_doubles.flip_card_stub import FlipCardNewStub, FlipCardFrontPlannedStub, \
    FlipCardBackPlannedStub


class FlipCardsRepositorySpy(FlipCardRepositoryInterface):

    def __init__(self):
        self.call_stack = []

    def save(self, flip_card: FlipCard):
        self.call_stack.append((self.save.__name__, flip_card))

    def draw_random_new_card(self) -> FlipCard:
        """pass"""

    def get_by_side_id(self, flip_card_side_id: FlipCardSideId) -> FlipCard:
        """pass"""


class FlipCardsRepositoryNewCardSpy(FlipCardsRepositorySpy):

    def draw_random_new_card(self) -> FlipCard:
        self.call_stack.append((self.draw_random_new_card.__name__,))
        return FlipCardNewStub()

    def get_by_side_id(self, flip_card_side_id: FlipCardSideId) -> FlipCard:
        """pass"""


class FlipCardsRepositoryFrontPlannedCardSpy(FlipCardsRepositorySpy):

    def draw_random_new_card(self) -> FlipCard:
        self.call_stack.append((self.draw_random_new_card.__name__,))
        return FlipCardFrontPlannedStub()

    def get_by_side_id(self, flip_card_side_id: FlipCardSideId) -> FlipCard:
        self.call_stack.append((self.get_by_side_id.__name__, flip_card_side_id))
        return FlipCardFrontPlannedStub()


class FlipCardsRepositoryBackPlannedCardSpy(FlipCardsRepositorySpy):

    def draw_random_new_card(self) -> FlipCard:
        self.call_stack.append((self.draw_random_new_card.__name__,))
        return FlipCardBackPlannedStub()

    def get_by_side_id(self, flip_card_side_id: FlipCardSideId) -> FlipCard:
        self.call_stack.append((self.get_by_side_id.__name__, flip_card_side_id))
        return FlipCardFrontPlannedStub()
