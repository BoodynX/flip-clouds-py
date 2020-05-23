from src.domain.events.abstractions.event import Event
from src.domain.services.event_log.listener_interface import ListenerInterface


class Listener_Spy(ListenerInterface):
    def __init__(self):
        self.call_stack = []

    def handle(self, event: Event):
        self.call_stack.append((Listener_Spy.handle.__name__, event))
