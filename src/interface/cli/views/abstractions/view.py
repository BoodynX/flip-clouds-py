from abc import ABC, abstractmethod

import click

from src.interface.cli.views.utils.printing_tools import pt


class View(ABC):
    @classmethod
    @abstractmethod
    def _template(cls) -> str:
        pass

    @classmethod
    def _print_view(cls, header: str, message: str):
        pt.wait_anim()
        pt.clear()
        pt.menu_header(text=header)
        pt.print(text=cls._template())
        cls._print_message(message)
        return click.getchar()

    @staticmethod
    def _print_message(message: str):
        if message:
            pt.print(text=message, fg='yellow')
        else:
            pt.print(text=' ')
