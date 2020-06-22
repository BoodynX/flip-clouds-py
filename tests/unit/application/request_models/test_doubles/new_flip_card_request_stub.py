from src.application.request_models.new_flip_card_request import NewFlipCardRequest
from tests.unit.domain.vos.test_doubles.sentence_stubs import Sentence_StubFrontPolish, Sentence_StubBackEnglish


class NewFlipCardRequest_Stub(NewFlipCardRequest):
    def __new__(cls, *args, **kwargs):
        return NewFlipCardRequest(
            front=Sentence_StubFrontPolish(),
            back=Sentence_StubBackEnglish()
        )
