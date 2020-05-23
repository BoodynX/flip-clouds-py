from abc import ABC

from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideId_StubFront, \
    FlipCardSideId_StubBack, FlipCardSideId_StubFront_Two


class UniqueFlipCardSidesContainer_StubAbstraction(UniqueFlipCardSidesContainer, ABC):
    def __init__(self):
        """pass"""


class UniqueFlipCardSidesContainer_StubMixedSides(UniqueFlipCardSidesContainer_StubAbstraction):
    value: set = {FlipCardSideId_StubFront(), FlipCardSideId_StubBack(), FlipCardSideId_StubFront_Two()}


class UniqueFlipCardSidesContainer_StubFrontSides(UniqueFlipCardSidesContainer_StubAbstraction):
    value: set = {FlipCardSideId_StubFront()}


class UniqueFlipCardSidesContainer_StubBackSides(UniqueFlipCardSidesContainer_StubAbstraction):
    value: set = {FlipCardSideId_StubBack()}
