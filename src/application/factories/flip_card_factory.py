from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from src.domain.entities.flip_card_side import FlipCardSide
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.vos.flip_card_id import FlipCardId
from src.domain.vos.flip_card_side_id import FlipCardSideId
from src.domain.vos.sentence import Sentence


class FlipCardFactory(FlipCardFactoryInterface):
    @classmethod
    def create_card(cls, front_sentence: Sentence, back_sentence: Sentence) -> FlipCard:
        front = FlipCardSide(
            id_=FlipCardSideId(uuid4()),
            sentence=front_sentence,
        )

        back = FlipCardSide(
            id_=FlipCardSideId(uuid4()),
            sentence=back_sentence,
        )

        return FlipCard(
            id_=FlipCardId(uuid4()),
            front=front,
            back=back,
        )
