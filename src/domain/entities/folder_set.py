from random import choice
from typing import Set
from uuid import UUID

from src.domain.entities.abstractions.entity import Entity
from src.domain.entities.card_folder import CardFolder


class FolderSet(Entity):
    def __init__(self, id_: UUID):
        self.id_ = id_
        self._folders: Set[CardFolder] = set()

    def add(self, folder: CardFolder):
        self._folders.add(folder)

    def pick_a_random_folder(self):
        if not self._folders:
            return None
        return choice(tuple(self._folders))