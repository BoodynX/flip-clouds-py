from src.interface.cli.controllers.abstractions.controller import Controller
from src.interface.cli.requests.abstractions.request import Request
from src.interface.cli.requests.card_manager_request import CardManagerRequest
from src.interface.cli.requests.main_menu_request import MainMenuRequest
from src.interface.cli.views.goodbye_screen import GoodbyeScreen
from src.interface.cli.views.main_menu_view import MainMenuView


class MainMenuController(Controller):
    @classmethod
    def show(cls) -> Request:
        return cls._route_request(option=MainMenuView.show())

    @classmethod
    def _route_request(cls, option: str):
        if option in ['1', '2']:
            next_option = MainMenuView.show(message='This is not available yet')
        elif option == '3':
            return CardManagerRequest()
        elif option.upper() == 'Q':
            return GoodbyeScreen.show()
        else:
            next_option = MainMenuView.show(message='No such option available')

        return MainMenuRequest(option=next_option)
