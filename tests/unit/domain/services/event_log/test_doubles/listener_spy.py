from src.domain.events.abstractions.event import Event
from src.domain.services.event_log.listener_interface import IListener


class Listener_Spy(IListener):
    def __init__(self):
        self.call_stack = []

    def handle(self, event: Event):
        self.call_stack.append((Listener_Spy.handle.__name__, event))
