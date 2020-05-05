from abc import abstractmethod, ABC
from random import choice

from src.domain.entities.flip_card import FlipCard
from src.domain.event_log import EventLog
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.card_side_state import CardSideState


class NewCardPickerInterface(ABC):
    @abstractmethod
    def draw_new_card(self):
        pass


class NewCardPicker(NewCardPickerInterface):
    def __init__(self, event_log: EventLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.event_log = event_log

    def draw_new_card(self) -> FlipCard:
        flip_card = self.repository.draw_random_new_card()

        if self._new_front_only_left_or_drawn(flip_card=flip_card):
            flip_card.front_state = CardSideState.StateType.DRAWN
        else:
            flip_card.back_state = CardSideState.StateType.DRAWN

        return flip_card

    @staticmethod
    def _new_front_only_left_or_drawn(flip_card: FlipCard) -> bool:
        new_front = flip_card.front_state.value == CardSideState.StateType.NEW
        new_back = flip_card.back_state.value == CardSideState.StateType.NEW
        return new_front and (not new_back or choice([True, False]))
