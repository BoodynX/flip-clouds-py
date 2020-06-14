from abc import ABC, abstractmethod

from src.domain.entities.flip_card import FlipCard


class IFlipCardRepository(ABC):
    @abstractmethod
    def save(self, flip_card: FlipCard):
        """pass"""

    @abstractmethod
    def get_new(self) -> FlipCard:
        """pass"""
