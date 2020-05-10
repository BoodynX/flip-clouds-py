from uuid import uuid4

from src.domain.vos.flip_card_side_id import FlipCardSideIdFront, FlipCardSideIdBack


class FlipCardSideIdFrontStub(FlipCardSideIdFront):
    def __init__(self):
        self.value = uuid4()


class FlipCardSideIdBackStub(FlipCardSideIdBack):
    def __init__(self):
        self.value = uuid4()
