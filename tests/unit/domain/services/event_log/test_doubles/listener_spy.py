from src.domain.events.abstractions.event import Event
from src.domain.services.event_log.listener_interface import ListenerInterface


class ListenerSpy(ListenerInterface):
    def __init__(self):
        self.call_stack = []

    def handle(self, event: Event):
        self.call_stack.append((ListenerSpy.handle.__name__, event))