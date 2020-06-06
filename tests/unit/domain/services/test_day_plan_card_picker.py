from unittest import TestCase

from tests.unit.domain.services.event_log.test_doubles.event_log_spy import EventLog_Spy


class TestDayPlanCardPicker(TestCase):
    def setUp(self):
        self.event_log = EventLog_Spy()