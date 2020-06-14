import click

from src.interface.cli.views.utils.printing_tools import pt


class MainMenuView:
    def show(self, message: str = '') -> str:
        pt.clear()
        pt.txt(text=self._template())
        self._print_message(message)
        return click.getchar()

    @staticmethod
    def _template() -> str:
        return '##############################\n' \
               'Welcome to Flip Clouds CLI! :)\n' \
               '##############################\n' \
               '\n' \
               '1 - Start learning today\'s flip cards\n' \
               '2 - Pick a new Card\n' \
               '3 - Add Card\n' \
               '\n' \
               'Q - Quit\n' \
               '\n'

    @staticmethod
    def _print_message(message: str):
        if message:
            pt.wait_anim()
            pt.txt(text=message, fg='yellow')
