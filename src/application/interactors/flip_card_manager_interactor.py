from src.application.factories.flip_card_factory import FlipCardFactory
from src.application.request_models.new_flip_card_request import NewFlipCardRequest
from src.domain.services.flip_card_manager import IFlipCardManager


class FlipCardManagerInteractor:
    def __init__(self, flip_card_manager: IFlipCardManager):
        self.flip_card_manager = flip_card_manager

    def add_card(self, request_model: NewFlipCardRequest):
        self.flip_card_manager.create_card(
            front=request_model.front,
            back=request_model.back,
            factory=FlipCardFactory
        )
