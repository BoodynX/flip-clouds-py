from abc import abstractmethod, ABC

from src.domain.entities.flip_card import FlipCard
from src.domain.entities.flip_card_side import FlipCardSide
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.services.event_log.event_log import EventLog


class NewFlipCardSidePickerInterface(ABC):
    @abstractmethod
    def draw_new_card_side(self) -> FlipCard:
        """pass"""


class NewFlipCardSidePicker(NewFlipCardSidePickerInterface):
    def __init__(self, event_log: EventLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.event_log = event_log

    def draw_new_card_side(self) -> FlipCardSide:
        flip_card_side = self.repository.draw_random_new_card_side()
        return flip_card_side
