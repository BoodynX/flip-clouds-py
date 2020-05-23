from src.domain.entities.flip_card import FlipCard
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.vos.sentence import Sentence
from tests.unit.domain.entities.test_doubles.flip_card_stubs import FlipCard_StubAllNew


class FlipCardFactory_Spy(FlipCardFactoryInterface):
    call_stack = []
    flip_card_stub = FlipCard_StubAllNew()

    @classmethod
    def create_card(cls, front: Sentence, back: Sentence) -> FlipCard:
        cls.call_stack.append((cls.create_card.__name__, (front, back)))
        return cls.flip_card_stub

    @classmethod
    def get_fresh_spy(cls):
        cls.call_stack = []
        cls.flip_card_stub = FlipCard_StubAllNew()
        return cls
