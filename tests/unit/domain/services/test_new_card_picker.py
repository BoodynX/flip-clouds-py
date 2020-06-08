from random import choice
from unittest import TestCase

from src.domain.entities.abstractions.entity import Entity
from src.domain.entities.flip_card import FlipCard
from src.domain.repositories.flip_card_repository_interface import FlipCardRepositoryInterface
from src.domain.vos.side import Side
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import FlipCardRepository_Spy


class CardFolder(Entity):
    def __init__(self, flip_card: FlipCard, side: Side):
        self.card = flip_card
        self.side = side


class NewCardPicker:
    def __init__(self, repository: FlipCardRepositoryInterface):
        self.repository = repository

    def get_new_flip_card_in_folder(self):
        flip_card = self.repository.get_new()
        side = choice((Side.front(), Side.back()))
        folder = CardFolder(flip_card=flip_card, side=side)
        # TODO put card folder in a new cards buffer
        return folder


class TestNewCardPicker(TestCase):
    def test_pick_new_card__return_card_in_folder_with_marked_side(self):
        self.flip_card_repository = FlipCardRepository_Spy()
        card_picker = NewCardPicker(self.flip_card_repository)

        folder = card_picker.get_new_flip_card_in_folder()

        # TODO check if card folder was added to buffer
        self.assertIsInstance(folder, CardFolder)
        self.assertEqual(folder.card, self.flip_card_repository.flip_card)
        self.assertIsInstance(folder.side, Side)
