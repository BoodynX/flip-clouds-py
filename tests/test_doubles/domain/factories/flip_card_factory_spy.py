from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.vos.sentence import Sentence


class FlipCardFactorySpy(FlipCardFactoryInterface):
    calls_stack = []

    @classmethod
    def create_card(cls, front: Sentence, back: Sentence):
        cls.calls_stack.append([front, back])
