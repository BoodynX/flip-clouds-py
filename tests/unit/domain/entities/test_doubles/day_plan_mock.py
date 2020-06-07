import inspect
from unittest.case import TestCase

from src.domain.entities.day_plan import IDayPlan
from src.domain.entities.flip_card import FlipCard
from src.domain.vos.side import Side
from tests.utils import CallStack


class DayPlan_Mock(TestCase, IDayPlan):
    def __init__(self):
        super().__init__()
        self.call_stack = CallStack()

    def add_flip_card(self, flip_card: FlipCard, side: Side):
        # TODO make a signature check helper
        print(inspect.signature(IDayPlan.add_flip_card) == inspect.signature(DayPlan_Mock.add_flip_card))
        self.call_stack.append(method=IDayPlan.add_flip_card, params={'flip_card': flip_card, 'side': side})

    def assert_flip_card_added_to_plan(self, call_number: int, flip_card: FlipCard, side: Side):
        call = self.call_stack.call(call_number)
        self.assertEqual(call.method, IDayPlan.add_flip_card)
        self.assertDictEqual(
            call.params,
            {'flip_card': flip_card, 'side': side}
        )