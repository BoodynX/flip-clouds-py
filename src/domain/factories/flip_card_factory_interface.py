from abc import ABC, abstractmethod

from src.domain.entities.flip_card import FlipCard
from src.domain.vos.sentence import Sentence


class FlipCardFactoryInterface(ABC):
    @classmethod
    @abstractmethod
    def create_card(cls, front: Sentence, back: Sentence) -> FlipCard:
        pass
