from unittest import TestCase

from src.domain.vos.abstractions.standard_value_object import StandardValueObject
from src.domain.vos.sentence import Sentence


class TestSentence(TestCase):
    sample_sentence = 'sample sentence'

    @classmethod
    def setUpClass(cls) -> None:
        cls.sentence = Sentence(cls.sample_sentence)

    def test_instance(self):
        self.assertIsInstance(self.sentence, Sentence)

    def test_input__empty_string__raise_exception(self):
        self.assertRaises(Sentence.InvalidSentence, Sentence, '')

    def test_input__whitespace_only__raise_exception(self):
        self.assertRaises(Sentence.InvalidSentence, Sentence, ' ')

    def test_input__none__raise_exception(self):
        self.assertRaises(StandardValueObject.InvalidValue, Sentence, None)

    def test_input__correct_value__store_in_param(self):
        self.assertEqual(self.sentence.value, self.sample_sentence)
