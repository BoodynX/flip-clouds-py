from src.interface.cli.requests.abstractions.request import Request
from src.interface.cli.requests.main_menu_request import MainMenuRequest
from src.interface.cli.views.main_menu_view import MainMenuView
from src.interface.cli.views.utils.printing_tools import pt


class Controller:
    pass


class MainMenuController(Controller):
    @staticmethod
    def handle(request: Request):
        option = request.option
        menu = MainMenuView()
        if option in ['1', '2', '3']:
            option = menu.show('This is not available yet')
        elif option in ['Q', 'q']:
            pt.clear()
            pt.heading(txt='Goodbye!')
            exit()
        else:
            option = menu.show('No such option available')

        return MainMenuRequest(option=option)


class Router:
    def __init__(self):
        self.routing_table = {
            MainMenuRequest: MainMenuController
        }

    def submit_request(self, request: Request):
        return self.routing_table[request.__class__].handle(request=request)


if __name__ == '__main__':
    Router().submit_request(MainMenuRequest('1'))
