from src.domain.vos.sentence import Sentence


class SentenceStubBack(Sentence):
    value = 'back sentence'

    def __init__(self):
        pass


class SentenceStubFront(Sentence):
    value = 'front sentence'

    def __init__(self):
        pass
