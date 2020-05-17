from unittest import TestCase

from src.domain.entities.box import Box
from src.domain.vos.primary_set import PrimarySet
from src.domain.vos.secondary_set import SecondarySet
from tests.unit.domain.vos.test_doubles.flip_card_side_id_stubs import FlipCardSideIdFrontStub, FlipCardSideIdBackStub


class TestBox(TestCase):
    def test_adding_ids_to_box_sets__ids_in_sets(self):
        box = Box(PrimarySet(set()), SecondarySet(set()))
        side_id_front = FlipCardSideIdFrontStub()
        side_id_back = FlipCardSideIdBackStub()

        box.add_to_primary(flip_card_side_id=side_id_front)
        box.add_to_secondary(flip_card_side_id=side_id_back)

        self.assertTrue(side_id_front in box._primary_set.value)
        self.assertTrue(side_id_back in box._secondary_set.value)

