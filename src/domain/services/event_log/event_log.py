from typing import List, Type

from src.domain.events.abstractions.event import Event
from src.domain.services.event_log.listener_interface import IListener


class EventLog:
    def __init__(self):
        self._subscribers = {}

    def fire(self, event: Event):
        event_name = event.__class__.__name__
        if event_name not in self._subscribers:
            return

        listeners: List[IListener] = self._subscribers[event_name]
        for listener in listeners:
            listener.handle(event=event)

    def subscribe(self, listener: IListener, event_type: Type[Event]):
        if event_type.__name__ not in self._subscribers:
            self._subscribers[event_type.__name__] = [listener]

            return

        if listener in self._subscribers[event_type.__name__]:
            raise self.ListenerAlreadySubscribedToEvent()

        self._subscribers[event_type.__name__].append(listener)

    class ListenerAlreadySubscribedToEvent(Exception):
        """pass"""
