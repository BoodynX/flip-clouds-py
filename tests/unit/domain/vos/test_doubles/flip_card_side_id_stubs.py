from abc import ABC
from uuid import uuid4

from src.domain.vos.flip_card_side_id import FlipCardSideId


class FlipCardSide_StubAbstraction(FlipCardSideId, ABC):
    def __init__(self):
        """pass"""


class FlipCardSideId_StubFront(FlipCardSide_StubAbstraction):
    value = uuid4()


class FlipCardSideId_StubFront_Two(FlipCardSide_StubAbstraction):
    value = uuid4()


class FlipCardSideId_StubBack(FlipCardSide_StubAbstraction):
    value = uuid4()

