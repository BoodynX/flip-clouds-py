from uuid import uuid4

from src.domain.entities.flip_card import FlipCard
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.flip_card_id import FlipCardId
from src.domain.vos.sentence import Sentence


class FlipCardFactory(FlipCardFactoryInterface):
    @classmethod
    def create_card(cls, front: Sentence, back: Sentence) -> FlipCard:
        return FlipCard(
            id_=FlipCardId(uuid4()),
            front_id=uuid4(),
            front=front,
            back_id=uuid4(),
            back=back,
            front_state=CardSideState(CardSideState.StateType.NEW),
            back_state=CardSideState(CardSideState.StateType.NEW)
        )
