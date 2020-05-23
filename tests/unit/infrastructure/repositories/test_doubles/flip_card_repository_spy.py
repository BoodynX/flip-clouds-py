from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.flip_card_side_id import FlipCardSideId
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_StubAllNew, \
    FlipCard_StubFrontPlannedBackNew, FlipCard_StubFrontNewBackPlanned


class FlipCardsRepository_Spy(FlipCardRepositoryInterface):

    def __init__(self):
        self.call_stack = []

    def save(self, flip_card: FlipCard):
        self.call_stack.append((self.save.__name__, flip_card))

    def draw_random_new_card(self) -> FlipCard:
        """pass"""

    def get_by_side_id(self, flip_card_side_id: FlipCardSideId) -> FlipCard:
        """pass"""


class FlipCardsRepository_SpyOnlyDrawAllNewCard(FlipCardsRepository_Spy):

    def draw_random_new_card(self) -> FlipCard:
        self.call_stack.append((self.draw_random_new_card.__name__,))
        return FlipCard_StubAllNew()

    def get_by_side_id(self, flip_card_side_id: FlipCardSideId) -> FlipCard:
        """pass"""


class FlipCardsRepository_SpyFrontPlannedBackNew(FlipCardsRepository_Spy):

    def draw_random_new_card(self) -> FlipCard:
        self.call_stack.append((self.draw_random_new_card.__name__,))
        return FlipCard_StubFrontPlannedBackNew()

    def get_by_side_id(self, flip_card_side_id: FlipCardSideId) -> FlipCard:
        self.call_stack.append((self.get_by_side_id.__name__, flip_card_side_id))
        return FlipCard_StubFrontPlannedBackNew()


class FlipCardsRepository_SpyFrontNewBackPlanned(FlipCardsRepository_Spy):

    def draw_random_new_card(self) -> FlipCard:
        self.call_stack.append((self.draw_random_new_card.__name__,))
        return FlipCard_StubFrontNewBackPlanned()

    def get_by_side_id(self, flip_card_side_id: FlipCardSideId) -> FlipCard:
        self.call_stack.append((self.get_by_side_id.__name__, flip_card_side_id))
        return FlipCard_StubFrontNewBackPlanned()
