from uuid import UUID

from src.interface.http.contexts.flip_card_manager.routes import ADD_CARD
from tests.system.http.abstractions.system_test import SystemTest


class TestFlipCardManager(SystemTest):
    def test_add_card__card_stored_in_db(self):
        json_payload = {
            "front": "co jest?",
            "back": "what's up?"
        }

        response = self.client.post(
            url=ADD_CARD,
            json=json_payload
        )

        self.assertEqual(response.status_code, 201)
        self._assert_valid_response_payload(json_payload, response)

    def _assert_valid_response_payload(self, json_payload, response):
        response_json = response.json()
        self.assertTrue(UUID(response_json['id_'], version=4))
        self.assertEqual(response_json['front'], json_payload['front'])
        self.assertEqual(response_json['back'], json_payload['back'])
