from unittest import TestCase

from fastapi.testclient import TestClient

from main import app
from src.interface.http.routes import ROOT


class TestMain(TestCase):
    def test_read_main(self):
        client = TestClient(app)
        response = client.get(ROOT)

        assert response.status_code == 200
        assert response.json() == {'message': 'Hello World'}

