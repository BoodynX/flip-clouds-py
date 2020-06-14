from abc import ABC, abstractmethod

from src.interface.cli.requests.abstractions.request import Request


class Controller(ABC):
    @classmethod
    @abstractmethod
    def show(cls) -> str:
        pass

    @classmethod
    def handle(cls, request: Request):
        if request.option:
            return cls._make_request(option=request.option)
        return cls._make_request(option=cls.show())

    @classmethod
    @abstractmethod
    def _make_request(cls, option: str) -> Request:
        pass
