from uuid import uuid4

from src.domain.vos.flip_card_id import FlipCardId


class FlipCardIdStub(FlipCardId):
    value = uuid4()

    def __init__(self):
        """pass"""
