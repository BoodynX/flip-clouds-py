from abc import ABC
from uuid import uuid4

from src.domain.vos.flip_card_side_id import FlipCardSideId


class FlipCardSideId_StubAbstraction(FlipCardSideId, ABC):
    def __init__(self):
        """pass"""


class FlipCardSideId_StubFront(FlipCardSideId_StubAbstraction):
    value = uuid4()


class FlipCardSideId_StubFront_Two(FlipCardSideId_StubAbstraction):
    value = uuid4()


class FlipCardSideId_StubBack(FlipCardSideId_StubAbstraction):
    value = uuid4()

