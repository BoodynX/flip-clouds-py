from src.interface.http.bootstrap_http import router
from src.interface.http.flip_card_manager.conroller.new_flip_card_controller import NewFlipCardController
from src.interface.http.flip_card_manager.requests.new_flip_card_request import NewFlipCardRequestModel
from src.interface.http.flip_card_manager.responses.new_flip_card import NewFlipCardResponseModel

ADD_CARD = '/flip_card_manager/add_card'


@router.post(ADD_CARD, status_code=201, response_model=NewFlipCardResponseModel)
def add_card(request: NewFlipCardRequestModel):
    return NewFlipCardController().add_card(request_model=request)
