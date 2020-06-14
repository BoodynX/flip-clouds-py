from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from src.domain.factories.flip_card_factory_interface import IFlipCardFactory
from src.domain.vos.flip_card_id import FlipCardId
from src.domain.vos.sentence import Sentence


class FlipCardFactory(IFlipCardFactory):
    @classmethod
    def create_card(cls, front: Sentence, back: Sentence) -> FlipCard:
        return FlipCard(
            id_=FlipCardId(uuid4()),
            front=front,
            back=back,
        )
