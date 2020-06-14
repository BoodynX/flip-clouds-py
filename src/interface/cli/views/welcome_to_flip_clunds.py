from src.interface.cli.views.utils.printing_tools import pt


class Welcome:
    @staticmethod
    def show():
        pt.clear()
        pt.heading('Flip Clouds')
        pt.wait_anim(length=55, tempo=0.03, unit='█')
