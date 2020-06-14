from src.interface.cli.views.utils.printing_tools import pt


class WelcomeScreen:
    @classmethod
    def show(cls):
        pt.clear()
        pt.banner('Flip Clouds')
        pt.wait_anim_alternative(length=55, tempo=0.01, unit='█')
