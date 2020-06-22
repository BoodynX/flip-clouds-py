from unittest import TestCase

from src.application.factories.flip_card_factory import FlipCardFactory
from src.application.interactors.flip_card_manager_interactor import FlipCardInteractor
from src.domain.services.flip_card_manager import IFlipCardManager
from tests.unit.application.request_models.test_doubles.new_flip_card_request_stub import NewFlipCardRequest_Stub
from tests.unit.domain.services.test_doubles.flip_card_manager_spy import FlipCardManager_Spy


class TestFlipCardManagerInteractor(TestCase):
    def test_add_card__card_saved_in_repository(self):
        self.new_flip_card_request = NewFlipCardRequest_Stub()
        self.flip_card_manager = FlipCardManager_Spy()
        interactor = FlipCardInteractor(
            flip_card_manager=self.flip_card_manager
        )

        interactor.add_card(request=self.new_flip_card_request)

        self._assert_sentences_passed_to_flip_card_manager()

    def _assert_sentences_passed_to_flip_card_manager(self):
        call = self.flip_card_manager.call_stack.call(1)
        expected_params = {
            'front': self.new_flip_card_request.front,
            'back': self.new_flip_card_request.back,
            'factory': FlipCardFactory
        }

        self.assertEqual(call.method, IFlipCardManager.create_card)
        self.assertDictEqual(call.params, expected_params)
