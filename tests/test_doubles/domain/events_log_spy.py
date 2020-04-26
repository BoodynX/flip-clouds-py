from src.domain.events.abstractions.event import Event
from src.domain.events_log import EventsLog


class EventLogSpy(EventsLog):
    def __init__(self):
        self.calls_stack = []

    def register(self, event: Event):
        self.calls_stack.append(event)