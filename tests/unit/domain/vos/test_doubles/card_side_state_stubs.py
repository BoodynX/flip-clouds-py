from src.domain.vos.card_side_state import CardSideState


class CardSideState_StubNew(CardSideState):
    value = CardSideState.StateType(CardSideState.StateType.NEW)

    def __init__(self):
        """pass"""


class CardSideState_StubPlanned(CardSideState):
    value = CardSideState.StateType(CardSideState.StateType.PLANNED)

    def __init__(self):
        """pass"""


class CardSideState_StubDrawn(CardSideState):
    value = CardSideState.StateType(CardSideState.StateType.DRAWN)

    def __init__(self):
        """pass"""
