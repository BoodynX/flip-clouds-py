from src.domain.events.abstractions.event import Event
from src.domain.event_log import EventLog


class EventLogSpy(EventLog):
    def __init__(self):
        self.call_stack = []

    def register(self, event: Event):
        self.call_stack.append([self.register.__name__, event])
