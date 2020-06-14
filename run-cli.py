import click

from src.interface.cli.requests.main_menu_request import MainMenuRequest
from src.interface.cli.services.router import Router
from src.interface.cli.views.main_menu_view import MainMenuView
from src.interface.cli.views.utils.printing_tools import pt
from src.interface.cli.views.welcome_to_flip_clunds import Welcome


@click.command()
def flip_cards_start():
    Welcome.show()
    menu = MainMenuView()
    option = menu.show()
    request = MainMenuRequest(option=option)
    router = Router()

    while True:
        request = router.submit_request(request)


if __name__ == '__main__':
    flip_cards_start()
