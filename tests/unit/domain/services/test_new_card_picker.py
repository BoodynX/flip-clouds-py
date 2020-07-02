from random import choice
from unittest import TestCase

from src.domain.repositories.i_flip_card_repository import IFlipCardRepository
from src.domain.vos.card_folder import CardFolder
from src.domain.vos.side import Side
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardRepository_Spy


class NewCardPicker:
    def __init__(self, repository: IFlipCardRepository):
        self.repository = repository

    def get_new_flip_card_in_folder(self):
        flip_card = self.repository.get_new()
        side = choice((Side.front(), Side.back()))
        folder = CardFolder(card=flip_card, side=side)

        # TODO put card folder in a NewCardsPlan
        return folder


class TestNewCardPicker(TestCase):
    def test_pick_new_card__return_card_in_folder_with_marked_side(self):
        self.flip_card_repository = FlipCardRepository_Spy()
        card_picker = NewCardPicker(self.flip_card_repository)

        folder = card_picker.get_new_flip_card_in_folder()

        # TODO check if card folder was added to folder_set
        self.assertIsInstance(folder, CardFolder)
        self.assertEqual(folder.card, self.flip_card_repository.flip_card)
        self.assertIsInstance(folder.side, Side)
