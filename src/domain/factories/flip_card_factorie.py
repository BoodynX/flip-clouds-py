from abc import ABC, abstractmethod

from src.domain.entities.flip_card import FlipCard
from src.domain.vos.sentence import Sentence


class FlipCardFactory(ABC):
    @abstractmethod
    def create_card(self, front: Sentence, back: Sentence) -> FlipCard:
        pass
