from src.domain.events.abstractions.event import Event
from src.domain.events_log import EventsLog


class EventLogSpy(EventsLog):
    def __init__(self):
        self.call_stack = []

    def register(self, event: Event):
        self.call_stack.append(event)
