from abc import ABC, abstractmethod

from src.domain.vos.sentence import Sentence


class FlipCardFactoryInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_card(front: Sentence, back: Sentence) -> 'FlipCard':
        pass
