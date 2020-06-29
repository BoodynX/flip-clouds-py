from src.application.factories.flip_card_factory import FlipCardFactory
from src.application.requests.new_flip_card_request import NewFlipCardRequest
from src.application.responses.new_flip_card_response import NewFlipCardResponse
from src.domain.entities.flip_card import FlipCard
from src.domain.services.flip_card_manager import IFlipCardManager


class FlipCardManagerInteractor:
    def __init__(self, flip_card_manager: IFlipCardManager):
        self.flip_card_manager = flip_card_manager

    def add_card(self, request: NewFlipCardRequest) -> NewFlipCardResponse:
        flip_card: FlipCard = self.flip_card_manager.create_card(
            front=request.front,
            back=request.back,
            factory=FlipCardFactory
        )

        return NewFlipCardResponse(
            id_=flip_card.id_.value,
            front=flip_card.front,
            back=flip_card.back
        )