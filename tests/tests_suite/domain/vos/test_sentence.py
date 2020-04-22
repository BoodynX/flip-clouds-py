from unittest import TestCase

from src.domain.vos.sentence import Sentence


class TestSentence(TestCase):
    def test_instance(self):
        sentence = Sentence(' ')
        self.assertIsInstance(sentence, Sentence)


"""
Test:
- empty string
- whitespaces only
- None
"""
