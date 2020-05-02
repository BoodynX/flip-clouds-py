from random import choice
from typing import Set, Type

from src.domain.entities.flip_card import FlipCard
from src.domain.events.new_card_created import NewCardCreated
from src.domain.events_log import EventsLog
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.sentence import Sentence
from src.domain.entities.day_plan import DayPlan


class FlipCardService:
    def __init__(self, events_log: EventsLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.events_log = events_log

    def create_card(self, front: Sentence, back: Sentence, factory: Type[FlipCardFactoryInterface]):
        flip_card: FlipCard = factory.create_card(front=front, back=back)
        self.repository.save(flip_card=flip_card)
        self.events_log.register(event=NewCardCreated(flip_card=flip_card))

    def draw_new_card(self) -> FlipCard:
        flip_card = self.repository.draw_random_new_card()
        return flip_card

    def draw_card_from_plan(self, day_plan: DayPlan) -> FlipCard:
        flip_card_id = choice(tuple(day_plan.flip_card_ids))
        return self.repository.get_card(id_=flip_card_id)
