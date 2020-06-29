from src.application.interactors.flip_card_manager_interactor import FlipCardManagerInteractor
from src.application.requests.new_flip_card_request import NewFlipCardRequest
from src.application.responses.new_flip_card_response import NewFlipCardResponse
from src.domain.services.event_log.event_log import EventLog
from src.domain.services.flip_card_manager import FlipCardManager
from src.domain.vos.sentence import Sentence
from src.interface.http.flip_card_manager.requests.new_flip_card_request import NewFlipCardRequestModel
from src.interface.http.flip_card_manager.responses.new_flip_card import NewFlipCardResponseModel
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardRepository_Spy


class NewFlipCardController:
    def add_card(self, request_model: NewFlipCardRequestModel):
        manager = FlipCardManager(
            event_log=EventLog(),
            # TODO implement actual Repository
            repository=FlipCardRepository_Spy()
        )
        interactor = FlipCardManagerInteractor(flip_card_manager=manager)

        request = NewFlipCardRequest(
            front=Sentence(request_model.front),
            back=Sentence(request_model.back)
        )

        response: NewFlipCardResponse = interactor.add_card(request=request)

        return {
            'id_': str(response.id_),
            'front': response.front.value,
            'back': response.back.value,
        }
