from unittest import TestCase
from uuid import uuid4

from src.domain.entities.filp_card import FlipCard
from tests.mocks.domain.vos.SentenceBackStub import SentenceBackStub
from tests.mocks.domain.vos.SentenceFrontStub import SentenceFrontStub


class TestFlipCard(TestCase):
    def test_instance(self):
        self.flip_card = FlipCard(id_=uuid4(), front=SentenceFrontStub(), back=SentenceBackStub())
