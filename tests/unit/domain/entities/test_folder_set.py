from unittest import TestCase
from uuid import uuid4

from src.domain.entities.card_folder import CardFolder
from src.domain.entities.folder_set import FolderSet
from tests.unit.domain.entities.test_doubles.card_folder_stub import CardFolder_Stub


class TestFolderSet(TestCase):
    def setUp(self):
        self.folder = CardFolder_Stub()
        self.folder_set = FolderSet(uuid4())

    def test_create_empty_folder_set__return_empty_folder(self):
        self.assertIsInstance(self.folder_set, FolderSet)

    def test_add_folder_to_empty_set__folder_in_set(self):
        self.folder_set.add(folder=self.folder)

        self.assertEqual(self.folder_set.pick_a_random_folder(), self.folder)

    def test_pick_from_empty_set__return_none(self):
        self.assertIsNone(self.folder_set.pick_a_random_folder())

    def test_submit_duplicate_folder__silently_omit(self):
        self.folder_set.add(self.folder)
        self.folder_set.add(self.second_folder_with_the_same_id())

        self.assertCountEqual(self.folder_set._folders, {self.folder})

    def second_folder_with_the_same_id(self) -> CardFolder:
        second_card_folder = CardFolder_Stub()
        second_card_folder.id_ = self.folder.id_
        return second_card_folder
