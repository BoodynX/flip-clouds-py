from src.interface.cli.controllers.abstractions.controller import Controller
from src.interface.cli.controllers.main_menu_controller import CardManagerRequest
from src.interface.cli.requests.abstractions.request import Request
from src.interface.cli.requests.main_menu_request import MainMenuRequest
from src.interface.cli.views.card_manager_view import CardManagerView


class CardManagerController(Controller):
    @classmethod
    def show(cls) -> str:
        return CardManagerView.show()

    @classmethod
    def _make_request(cls, option: str) -> Request:
        if option == '1':
            next_option = CardManagerView.show(message='This is not available yet')
        elif option.upper() == 'M':
            return MainMenuRequest()
        else:
            next_option = CardManagerView.show(message='No such option')

        return CardManagerRequest(option=next_option)

