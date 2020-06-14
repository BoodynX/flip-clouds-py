from abc import ABC, abstractmethod

from src.domain.events.abstractions.event import Event


class IListener(ABC):
    @abstractmethod
    def handle(self, event: Event):
        """pass"""
