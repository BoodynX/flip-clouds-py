from uuid import uuid4

from src.domain.vos.flip_card_side_id import FlipCardSideIdFront, FlipCardSideIdBack, FlipCardSideId


class FlipCardSideIdFrontStub(FlipCardSideIdFront):
    def __init__(self):
        self.value = uuid4()


class FlipCardSideIdBackStub(FlipCardSideIdBack):
    def __init__(self):
        self.value = uuid4()


class FlipCardSideIdStub(FlipCardSideId):
    value = uuid4()

    def __new__(cls, *args, **kwargs):
        return FlipCardSideId(value=cls.value)