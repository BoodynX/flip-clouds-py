from src.interface.cli.controllers.abstractions.controller import Controller
from src.interface.cli.requests.card_manager_request import CardManagerRequest
from src.interface.cli.requests.abstractions.request import Request
from src.interface.cli.requests.main_menu_request import MainMenuRequest
from src.interface.cli.views.card_manager.card_manager_view import CardManagerView
from src.interface.cli.views.goodbye_screen import GoodbyeScreen


class CardManagerController(Controller):
    @classmethod
    def show(cls) -> Request:
        return cls._route_request(option=CardManagerView.show())

    @classmethod
    def _route_request(cls, option: str) -> Request:
        if option == '1':
            next_option = CardManagerView.show(message='This is not available yet')
        elif option.upper() == 'M':
            return MainMenuRequest()
        elif option.upper() == 'Q':
            return GoodbyeScreen.show()
        else:
            next_option = CardManagerView.show(message='No such option')

        return CardManagerRequest(option=next_option)

