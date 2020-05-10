from unittest import TestCase

from src.domain.entities.new_card_sides_buffer import NewCardSidesBuffer
from src.domain.vos.primary_set import PrimarySet
from src.domain.vos.secondary_set import SecondarySet
from tests.unit.domain.vos.test_doubles.flip_card_side_id_test_doubles import FlipCardSideIdFrontStub, FlipCardSideIdBackStub


class TestNewCardSidesBuffer(TestCase):
    def test_adding_ids_to_buffer_sets__ids_in_sets(self):
        buffer = NewCardSidesBuffer(PrimarySet(set()), SecondarySet(set()))
        side_id_front = FlipCardSideIdFrontStub()
        side_id_back = FlipCardSideIdBackStub()

        buffer.add_to_primary(flip_card_side_id=side_id_front)
        buffer.add_to_secondary(flip_card_side_id=side_id_back)

        self.assertTrue(side_id_front in buffer.primary_set.value)
        self.assertTrue(side_id_back in buffer.secondary_set.value)

