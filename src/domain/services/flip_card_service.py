from random import choice
from typing import Type

from src.domain.entities.day_plan import DayPlan
from src.domain.entities.flip_card import FlipCard
from src.domain.event_log import EventLog
from src.domain.events.new_card_created import NewCardCreated
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.card_side_state import CardSideState
from src.domain.vos.sentence import Sentence


class FlipCardService:
    def __init__(self, event_log: EventLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.event_log = event_log

    def create_card(self, front: Sentence, back: Sentence, factory: Type[FlipCardFactoryInterface]):
        flip_card: FlipCard = factory.create_card(front=front, back=back)
        self.repository.save(flip_card=flip_card)
        self.event_log.register(event=NewCardCreated(flip_card=flip_card))

    def draw_new_card(self) -> FlipCard:
        flip_card = self.repository.draw_random_new_card()

        if self._new_front_only_left_or_drawn(flip_card):
            flip_card.front_state = CardSideState.StateType.DRAWN
        else:
            flip_card.back_state = CardSideState.StateType.DRAWN

        return flip_card

    def draw_card_from_plan(self, day_plan: DayPlan) -> FlipCard:
        # TODO Draw side id instead !!!
        flip_card_id = choice(tuple(day_plan.flip_card_ids))
        # TODO get flip card base on side id !!!
        return self.repository.get(id_=flip_card_id)

    @staticmethod
    def _new_front_only_left_or_drawn(flip_card: FlipCard) -> bool:
        new_front = flip_card.front_state.value == CardSideState.StateType.NEW
        new_back = flip_card.back_state.value == CardSideState.StateType.NEW
        return new_front and (not new_back or choice([True, False]))
