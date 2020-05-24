from unittest import TestCase

from src.domain.entities.day_plan import DayPlan
from src.domain.entities.flip_card import FlipCard
from src.domain.services.day_plan_card_picker import DayPlanCardPicker
from src.domain.vos.card_side_state import CardSideState
from tests.unit.domain.entities.test_doubles.day_plan_stubs import DayPlan_StubFrontSides, \
    DayPlan_StubBackSides
from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLog_Spy
from tests.unit.infrastructure.repositories.test_doubles.flip_card_repository_spy import \
    FlipCardsRepository_SpyFrontPlannedBackNew, FlipCardsRepository_SpyFrontNewBackPlanned, FlipCardsRepository_Spy


class TestDayPlanCardPicker(TestCase):
    def setUp(self):
        self.event_log = EventLog_Spy()

    def test_drawing_front_side_id_from_day_plan__return_flip_card(self):
        day_plan = DayPlan_StubFrontSides()
        repository = FlipCardsRepository_SpyFrontPlannedBackNew()
        card_picker = DayPlanCardPicker(event_log=self.event_log, repository=repository)

        flip_card = card_picker.draw_card_from_plan(day_plan=day_plan)

        self._assert_flip_cards_front_side_was_marked_as_drawn(flip_card)
        self._assert_repository_called_with_side_id_from_day_plan(day_plan=day_plan, repository=repository)

    def test_drawing_back_side_id_from_day_plan__return_flip_card(self):
        day_plan = DayPlan_StubBackSides()
        repository = FlipCardsRepository_SpyFrontNewBackPlanned()
        card_picker = DayPlanCardPicker(event_log=self.event_log, repository=repository)

        flip_card = card_picker.draw_card_from_plan(day_plan=day_plan)

        self._assert_flip_cards_back_side_was_marked_as_drawn(flip_card=flip_card)
        self._assert_repository_called_with_side_id_from_day_plan(day_plan=day_plan, repository=repository)

    def _assert_flip_cards_back_side_was_marked_as_drawn(self, flip_card: FlipCard):
        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(flip_card.back_state.value, CardSideState.StateType.DRAWN)
        self.assertNotEqual(flip_card.front_state.value, CardSideState.StateType.DRAWN)

    def _assert_flip_cards_front_side_was_marked_as_drawn(self, flip_card):
        self.assertIsInstance(flip_card, FlipCard)
        self.assertEqual(flip_card.front_state.value, CardSideState.StateType.DRAWN)
        self.assertNotEqual(flip_card.back_state.value, CardSideState.StateType.DRAWN)

    def _assert_repository_called_with_side_id_from_day_plan(self, day_plan: DayPlan,
                                                             repository: FlipCardsRepository_Spy):
        called_method = repository.call_stack[0][0]
        expected_method_call = repository.get_by_side_id.__name__
        submitted_day_plan_id = repository.call_stack[0][1]

        self.assertEqual(called_method, expected_method_call)
        self.assertIn(submitted_day_plan_id, day_plan._unique_flip_card_sides_container.value)