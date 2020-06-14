from src.interface.cli.views.utils.printing_tools import pt


class GoodbyeScreen:
    @classmethod
    def show(cls):
        pt.clear_line()
        pt.wait_anim()
        pt.clear()
        pt.banner(text='Goodbye!')
        exit()
