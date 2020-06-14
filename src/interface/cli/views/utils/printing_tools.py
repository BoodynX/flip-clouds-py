from time import sleep

import click
from pyfiglet import Figlet


# AKA Printing Tools :)
class pt:
    THEME_COLOR = 'blue'
    TXT_COLOR = 'white'

    @classmethod
    def txt(cls, text: str, fg: str = None):
        if not fg:
            fg = cls.TXT_COLOR
        click.echo(click.style(text=text, fg=fg))

    @classmethod
    def heading(cls, txt: str, font: str = 'stop'):
        figlet = Figlet(font=font)
        cls.txt(text=figlet.renderText(txt), fg=cls.THEME_COLOR)

    @classmethod
    def wait_anim(cls, length: int = 4, tempo: float = 0.2, unit: str = '.'):
        bar = ''
        for _ in range(length):
            click.echo(click.style(text=bar, fg=cls.THEME_COLOR))
            sleep(tempo)
            cls.clear_line()
            bar = f'{bar}{unit}'

    @classmethod
    def clear(cls):
        click.clear()

    @classmethod
    def clear_line(cls):
        print('\033[A \033[A')  # clears one line
