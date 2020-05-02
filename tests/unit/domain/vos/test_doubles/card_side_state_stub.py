from src.domain.vos.card_side_state import CardSideState


class CardSideStateNewStub(CardSideState):
    value = CardSideState.StateType(CardSideState.StateType.NEW)

    def __init__(self):
        """pass"""


class CardSideStatePlannedStub(CardSideState):
    value = CardSideState.StateType(CardSideState.StateType.PLANNED)

    def __init__(self):
        """pass"""
