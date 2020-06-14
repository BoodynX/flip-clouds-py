from typing import Type

from src.domain.events.abstractions.event import Event
from src.domain.services.event_log.event_log import EventLog
from src.domain.services.event_log.listener_interface import IListener


class EventLog_Spy(EventLog):
    def __init__(self):
        self.call_stack = []

    def fire(self, event: Event):
        self.call_stack.append((self.fire.__name__, event))

    def subscribe(self, listener: IListener, event_type: Type[Event]):
        """pass"""
