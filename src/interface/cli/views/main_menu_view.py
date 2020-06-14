from src.interface.cli.views.abstractions.view import View


class MainMenuView(View):
    @classmethod
    def show(cls, message: str = '') -> str:
        header = 'Welcome to Flip Clouds CLI! :)'
        return cls._print_view(header, message)

    @classmethod
    def _template(cls) -> str:
        return '1 - Start learning today\'s flip cards\n' \
               '2 - Pick a new Card\n' \
               '3 - Add Card\n' \
               '\n' \
               'Q - Quit\n\n' \
