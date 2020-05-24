from unittest import TestCase

from src.domain.entities.box import Box
from src.domain.vos.primary_set import PrimarySet
from src.domain.vos.secondary_set import SecondarySet
from tests.unit.domain.entities.test_doubles.flip_card_side_stubs import FlipCardSide_StubFront, FlipCardSide_StubBack


class TestBox(TestCase):
    def test_adding_ids_to_box_sets__ids_in_sets(self):
        box = Box(PrimarySet(set()), SecondarySet(set()))
        side_front = FlipCardSide_StubFront()
        side_back = FlipCardSide_StubBack()

        box.add_to_primary(flip_card_side_id=side_front)
        box.add_to_secondary(flip_card_side_id=side_back)

        self.assertTrue(side_front in box._primary_set.value)
        self.assertTrue(side_back in box._secondary_set.value)

