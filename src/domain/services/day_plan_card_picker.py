from src.domain.entities.day_plan import DayPlan
from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.services.event_log.event_log import EventLog


class DayPlanCardPicker:
    def __init__(self, event_log: EventLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.event_log = event_log

    def draw_card_from_plan(self, day_plan: DayPlan) -> FlipCard:
        flip_card_side_id = day_plan.pick_random_flip_card_side_id()
        flip_card = self.repository.get_by_side_id(flip_card_side_id=flip_card_side_id)
        return flip_card

    class SideIdDoesNotBelongToCard(Exception):
        """pass"""
