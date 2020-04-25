from unittest import TestCase

from src.domain.vos.familiarity import Familiarity


class TestFamiliarity(TestCase):
    unknown_familiarity_level = 'unknown level'

    def test_creation__incorrect_level_submitted__raise_unknown_level_exception(self):
        self.assertRaises(Familiarity.InvalidFamiliarityLevel,
                          Familiarity,
                          self.unknown_familiarity_level)

    def test_creation__correct_level_submitted__return_instance(self):
        familiarity = Familiarity(Familiarity.Level.NONE)

        self.assertIsInstance(familiarity, Familiarity)
