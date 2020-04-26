from abc import ABC, abstractmethod

from src.domain.entities.flip_card import FlipCard


class FlipCardRepositoryInterface(ABC):
    @abstractmethod
    def save(self, flip_card: FlipCard):
        pass
