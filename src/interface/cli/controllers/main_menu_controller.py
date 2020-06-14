from src.interface.cli.controllers.abstractions.controller import Controller
from src.interface.cli.requests.abstractions.request import Request
from src.interface.cli.requests.card_manager_request import CardManagerRequest
from src.interface.cli.requests.main_menu_request import MainMenuRequest
from src.interface.cli.views.main_menu_view import MainMenuView
from src.interface.cli.views.utils.printing_tools import pt


class MainMenuController(Controller):
    @classmethod
    def handle(cls, request: Request) -> Request:
        if request.option:
            return cls._make_request(option=request.option)
        return cls.show()

    @classmethod
    def show(cls) -> Request:
        return cls._make_request(option=MainMenuView.show())

    @classmethod
    def _make_request(cls, option: str = ''):
        if option in ['1', '2']:
            return cls._main_menu_request(message='This is not available yet')
        elif option == '3':
            return CardManagerRequest()
        elif option.upper() == 'Q':
            pt.clear_line()
            pt.wait_anim()
            pt.clear()
            pt.banner(text='Goodbye!')
            exit()
        else:
            return cls._main_menu_request(message='No such option available')

    @classmethod
    def _main_menu_request(cls, message: str) -> Request:
        next_option = MainMenuView.show(message=message)
        return MainMenuRequest(option=next_option)
