from uuid import uuid4

from src.domain.vos.flip_card_id import FlipCardId


class FlipCardId_Stub(FlipCardId):
    value = uuid4()

    def __init__(self):
        """pass"""
