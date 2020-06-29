from unittest import TestCase

from starlette.testclient import TestClient

from main import app
from src.interface.http.flip_card_manager.routes import ADD_CARD


class TestFlipCardManager(TestCase):
    def test_add_card__card_stored_in_db(self):
        client = TestClient(app)
        json_payload = {
            "front": "co jest?",
            "back": "what's up?"
        }

        response = client.post(
            url=ADD_CARD,
            json=json_payload
        )

        response_json = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_json['front'], json_payload['front'])
        self.assertEqual(response_json['back'], json_payload['back'])
