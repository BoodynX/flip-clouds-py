from src.interface.cli.controllers.card_manager_controller import CardManagerController
from src.interface.cli.controllers.main_menu_controller import MainMenuController
from src.interface.cli.requests.card_manager_request import CardManagerRequest
from src.interface.cli.requests.abstractions.request import Request
from src.interface.cli.requests.main_menu_request import MainMenuRequest


class Router:
    def __init__(self):
        self.routing_table = {
            MainMenuRequest: MainMenuController,
            CardManagerRequest: CardManagerController,
        }

    def submit_request(self, request: Request):
        return self.routing_table[request.__class__].handle(request=request)
