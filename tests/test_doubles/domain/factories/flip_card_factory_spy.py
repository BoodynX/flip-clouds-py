from src.domain.entities.flip_card import FlipCard
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.vos.sentence import Sentence
from tests.test_doubles.domain.entities.flip_card_stub import FlipCardStub


class FlipCardFactorySpy(FlipCardFactoryInterface):
    call_stack = []

    @classmethod
    def create_card(cls, front: Sentence, back: Sentence) -> FlipCard:
        cls.call_stack.append([front, back])
        return FlipCardStub()
