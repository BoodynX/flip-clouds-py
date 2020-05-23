from uuid import uuid4

from src.domain.vos.flip_card_side_id import FlipCardSideId

front_uuid = uuid4()
back_uuid = uuid4()


class FlipCardSideIdFrontStub(FlipCardSideId):
    value = front_uuid

    def __new__(cls, *args, **kwargs):
        return FlipCardSideId(value=cls.value)


class FlipCardSideIdBackStub(FlipCardSideId):
    value = back_uuid

    def __new__(cls, *args, **kwargs):
        return FlipCardSideId(value=cls.value)


class FlipCardSideIdStub(FlipCardSideId):
    value = uuid4()

    def __new__(cls, *args, **kwargs):
        return FlipCardSideId(value=cls.value)


class FlipCardSideIdStubPolish(FlipCardSideId):
    value = front_uuid

    def __new__(cls, *args, **kwargs):
        return FlipCardSideId(value=cls.value)


class FlipCardSideIdStubEnglish(FlipCardSideId):
    value = back_uuid

    def __new__(cls, *args, **kwargs):
        return FlipCardSideId(value=cls.value)
