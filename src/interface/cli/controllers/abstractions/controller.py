from abc import ABC, abstractmethod

from src.interface.cli.requests.abstractions.request import Request


class Controller(ABC):
    @classmethod
    @abstractmethod
    def show(cls) -> Request:
        pass

    @classmethod
    def handle(cls, request: Request) -> Request:
        if request.option:
            return cls._route_request(option=request.option)
        return cls.show()

    @classmethod
    @abstractmethod
    def _route_request(cls, option: str) -> Request:
        pass
