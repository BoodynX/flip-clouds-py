import click

from src.interface.cli.controllers.main_menu_controller import MainMenuController
from src.interface.cli.services.router import Router
from src.interface.cli.views.welcome_screen import WelcomeScreen


@click.command()
def flip_cards_start():
    router = Router()
    WelcomeScreen.show()
    request = MainMenuController.show()

    while True:
        if request:
            request = router.submit_request(request)


if __name__ == '__main__':
    flip_cards_start()
