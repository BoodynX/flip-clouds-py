from src.interface.cli.views.abstractions.view import View


class CardManagerView(View):
    @classmethod
    def show(cls, message: str = '') -> str:
        return cls._print_view(header='CardManager', message=message)

    @classmethod
    def _template(cls) -> str:
        return '1 - Add Card\n' \
               '\n' \
               'M - Main Menu\n\n'
