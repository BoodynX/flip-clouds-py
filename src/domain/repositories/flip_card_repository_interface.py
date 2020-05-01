from abc import ABC, abstractmethod

from src.domain.entities.flip_card import FlipCard
from src.domain.vos.flip_card_id import FlipCardId


class FlipCardRepositoryInterface(ABC):
    @abstractmethod
    def save(self, flip_card: FlipCard):
        """pass"""

    @abstractmethod
    def draw_random_new_card(self) -> FlipCard:
        """pass"""

    @abstractmethod
    def get_card(self, id_: FlipCardId) -> FlipCard:
        """pass"""
