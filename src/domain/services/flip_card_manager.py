from typing import Type

from src.domain.entities.flip_card import FlipCard
from src.domain.services.event_log.event_log import EventLog
from src.domain.events.new_card_created import NewCardCreated
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.sentence import Sentence


class FlipCardManager:
    def __init__(self, event_log: EventLog, repository: FlipCardRepositoryInterface):
        self.repository = repository
        self.event_log = event_log

    def create_card(self, front: Sentence, back: Sentence, factory: Type[FlipCardFactoryInterface]):
        flip_card: FlipCard = factory.create_card(front=front, back=back)
        self.repository.save(flip_card=flip_card)
        self.event_log.fire(event=NewCardCreated(flip_card=flip_card))
