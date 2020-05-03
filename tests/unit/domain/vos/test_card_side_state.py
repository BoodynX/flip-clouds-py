from unittest import TestCase

from src.domain.vos.card_side_state import CardSideState


class TestCardSideState(TestCase):
    invalid_state = 'invalid state'

    def test_invalid_state_type__raise_exception(self):
        self.assertRaises(CardSideState.InvalidFlipCardStateType, CardSideState, self.invalid_state)
