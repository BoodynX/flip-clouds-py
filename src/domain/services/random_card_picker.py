from random import choice

from src.domain.entities.day_plan import DayPlan
from src.domain.entities.flip_card import FlipCard
from src.domain.event_log import EventLog
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.card_side_state import CardSideState


class RandomCardPicker:
    def __init__(self, event_log: EventLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.event_log = event_log

    def draw_new_card(self) -> FlipCard:
        flip_card = self.repository.draw_random_new_card()

        if self._new_front_only_left_or_drawn(flip_card=flip_card):
            flip_card.front_state = CardSideState.StateType.DRAWN
        else:
            flip_card.back_state = CardSideState.StateType.DRAWN

        return flip_card

    def draw_card_from_plan(self, day_plan: DayPlan) -> FlipCard:
        flip_card_side_id = self._select_random_flip_card_side_id(day_plan=day_plan)
        flip_card = self.repository.get_by_side_id(flip_card_side_id=flip_card_side_id)
        # TODO mark drawn card side
        return flip_card

    @staticmethod
    def _select_random_flip_card_side_id(day_plan: DayPlan):
        return choice(tuple(day_plan.flip_card_side_ids))

    @staticmethod
    def _new_front_only_left_or_drawn(flip_card: FlipCard) -> bool:
        new_front = flip_card.front_state.value == CardSideState.StateType.NEW
        new_back = flip_card.back_state.value == CardSideState.StateType.NEW
        return new_front and (not new_back or choice([True, False]))
