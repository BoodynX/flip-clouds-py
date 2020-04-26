from src.domain.entities.flip_card import FlipCard
from src.domain.events.abstractions.event import Event


class NewCardCreated(Event):
    def __init__(self, flip_card: FlipCard):
        self.flip_card = flip_card