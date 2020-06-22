from src.domain.vos.sentence import Sentence


class NewFlipCardRequest:
    def __init__(self, front: Sentence, back: Sentence):
        self.front = front
        self.back = back
