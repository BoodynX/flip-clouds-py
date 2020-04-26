from src.domain.entities.flip_card import FlipCard
from src.domain.events.abstractions.event import Event
from src.domain.events.new_card_created import NewCardCreated
from src.domain.events_log import EventsLog
from src.domain.factories.flip_card_factory_interface import FlipCardFactoryInterface
from src.domain.vos.sentence import Sentence


class FlipCardService:
    def __init__(self, events_log: EventsLog):
        self.events_log = events_log

    def create_card(self, front: Sentence, back: Sentence, factory: FlipCardFactoryInterface):
        flip_card: FlipCard = factory.create_card(front=front, back=back)
        event: Event = NewCardCreated(flip_card=flip_card)
        self.events_log.register(event=event)