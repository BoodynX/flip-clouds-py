from src.domain.vos.familiarity import Familiarity


class FamiliarityNoneStub(Familiarity):
    value = Familiarity.Level.NONE

    def __init__(self):
        pass
