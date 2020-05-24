from abc import ABC

from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer
from tests.unit.domain.entities.test_doubles.flip_card_side_stubs import FlipCardSide_StubFront, FlipCardSide_StubBack, \
    FlipCardSide_StubFront_Two


class UniqueFlipCardSidesContainer_StubAbstraction(UniqueFlipCardSidesContainer, ABC):
    def __init__(self):
        """pass"""


class UniqueFlipCardSidesContainer_StubMixedSides(UniqueFlipCardSidesContainer_StubAbstraction):
    value: set = {FlipCardSide_StubFront(), FlipCardSide_StubBack(), FlipCardSide_StubFront_Two()}


class UniqueFlipCardSidesContainer_StubFrontSides(UniqueFlipCardSidesContainer_StubAbstraction):
    value: set = {FlipCardSide_StubFront()}


class UniqueFlipCardSidesContainer_StubBackSides(UniqueFlipCardSidesContainer_StubAbstraction):
    value: set = {FlipCardSide_StubBack()}
