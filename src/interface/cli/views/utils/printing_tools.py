from time import sleep

import click
from pyfiglet import Figlet


# AKA Printing Tools :)
class pt:
    THEME_COLOR = 'blue'
    TXT_COLOR = 'white'
    ALTERNATIVE_ANIMATION_LOCK = False

    @classmethod
    def print(cls, text: str, fg: str = None):
        if not fg:
            fg = cls.TXT_COLOR
        click.echo(click.style(text=text, fg=fg))

    @classmethod
    def banner(cls, text: str, font: str = 'stop'):
        figlet = Figlet(font=font)
        cls.print(text=figlet.renderText(text), fg=cls.THEME_COLOR)

    @classmethod
    def menu_header(cls, text: str):
        header_len = len(text)
        header_frame_bar = ''
        for _ in range(header_len):
            header_frame_bar = f'{header_frame_bar}#'

        header = f'{header_frame_bar}\n' \
                 f'{text}\n' \
                 f'{header_frame_bar}\n\n'

        cls.print(text=header)

    @classmethod
    def wait_anim(cls, length: int = 4, tempo: float = 0.1, unit: str = '.'):
        if cls.ALTERNATIVE_ANIMATION_LOCK:
            cls.ALTERNATIVE_ANIMATION_LOCK = False
            return
        cls.clear_line()
        cls._wait_anim(length, tempo, unit)

    @classmethod
    def wait_anim_alternative(cls, length: int, tempo: float, unit: str):
        """This version puts a lock on next normal waiting animation,
         which is fired before the screen gets cleared"""
        cls._wait_anim(length, tempo, unit)
        cls.ALTERNATIVE_ANIMATION_LOCK = True

    @classmethod
    def _wait_anim(cls, length, tempo, unit):
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
        print('\033[A                                                               \033[A')  # clears one line
