from src.domain.vos.card_side_state import CardSideState


class CardSideStateStubNew(CardSideState):
    value = CardSideState.StateType(CardSideState.StateType.NEW)

    def __init__(self):
        """pass"""


class CardSideStateStubPlanned(CardSideState):
    value = CardSideState.StateType(CardSideState.StateType.PLANNED)

    def __init__(self):
        """pass"""


class CardSideStateStubDrawn(CardSideState):
    value = CardSideState.StateType(CardSideState.StateType.DRAWN)

    def __init__(self):
        """pass"""
