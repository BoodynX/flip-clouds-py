from datetime import datetime
from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.vos.familiarity import Familiarity
from src.domain.vos.sentence import Sentence


class FlipCardFactory(FlipCardFactoryInterface):
    @classmethod
    def create_card(cls, front: Sentence, back: Sentence) -> FlipCard:
        return FlipCard(
            id_=uuid4(),
            front=front,
            back=back,
            familiarity=Familiarity(Familiarity.Level.NONE),
            last_shown=datetime.now()
        )
