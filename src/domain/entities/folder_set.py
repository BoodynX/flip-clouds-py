from random import choice
from typing import Set, Union
from uuid import UUID

from src.domain.entities.abstractions.entity import Entity
from src.domain.vos.card_folder import CardFolder


class FolderSet(Entity):
    def __init__(self, id_: UUID):
        self.id_ = id_
        self._folders: Set[CardFolder] = set()

    def add(self, folder: CardFolder):
        self._folders.add(folder)

    def pick_a_random_folder(self) -> Union[CardFolder, None]:
        if not self._folders:
            return None
        return choice(tuple(self._folders))
