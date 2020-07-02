from unittest import TestCase

from starlette.testclient import TestClient

from main import app


class SystemTest(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.client = TestClient(app)
