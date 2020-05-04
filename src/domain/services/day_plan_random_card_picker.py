from random import choice

from src.domain.entities.day_plan import DayPlan
from src.domain.entities.flip_card import FlipCard
from src.domain.event_log import EventLog
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.flip_card_side_id import FlipCardSideIdFront, FlipCardSideId


class DayPlanRandomCardPicker:
    def __init__(self, event_log: EventLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.event_log = event_log

    def draw_card_from_plan(self, day_plan: DayPlan) -> FlipCard:
        flip_card_side_id = self._select_random_flip_card_side_id(day_plan=day_plan)
        flip_card = self.repository.get_by_side_id(flip_card_side_id=flip_card_side_id)
        flip_card = self._mark_drawn_side(flip_card, flip_card_side_id)
        return flip_card

    @staticmethod
    def _mark_drawn_side(flip_card: FlipCard, flip_card_side_id: FlipCardSideId) -> FlipCard:
        drawn = CardSideState(CardSideState.StateType.DRAWN)
        if isinstance(flip_card_side_id, FlipCardSideIdFront):
            flip_card.front_state = drawn
        else:
            flip_card.back_state = drawn
        return flip_card

    @staticmethod
    def _select_random_flip_card_side_id(day_plan: DayPlan):
        return choice(tuple(day_plan.flip_card_side_ids))
