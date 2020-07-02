from src.interface.http.contexts.flip_card_manager.routes import ADD_CARD
from tests.system.http.abstractions.system_test import SystemTest


class TestVoInvalidValueHandler(SystemTest):
    def setUp(self) -> None:
        self.INVALID_SENTENCE = '>'

    def test_invalid_sentence__return_422_status_code(self):
        json_payload = {
            "front": self.INVALID_SENTENCE,
            "back": self.INVALID_SENTENCE
        }

        self.response = self.client.post(
            url=ADD_CARD,
            json=json_payload
        )

        self.assertEqual(self.response.status_code, 422)
        self._assert_valid_response_payload()

    def _assert_valid_response_payload(self):
        expected_response = {
            'detail': [{
                'loc': [''],
                'msg': "InvalidSentence: '>'",
                'type': 'type_error.invalid_data_format'
                }
            ]
        }

        self.assertDictEqual(expected_response, self.response.json())
