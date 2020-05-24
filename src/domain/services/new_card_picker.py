from abc import abstractmethod, ABC

from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.services.event_log.event_log import EventLog


class NewCardPickerInterface(ABC):
    @abstractmethod
    def draw_new_card(self) -> FlipCard:
        """pass"""


class NewCardPicker(NewCardPickerInterface):
    def __init__(self, event_log: EventLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.event_log = event_log

    def draw_new_card(self) -> FlipCard:
        flip_card = self.repository.draw_random_new_card()
        return flip_card
