from unittest.case import TestCase

from src.domain.services.event_log.event_log import EventLog
from tests.unit.domain.events.test_doubles.event_dummies import Event_Dummy, Event_DummySecond
from tests.unit.domain.services.event_log.test_doubles.listener_spy import Listener_Spy


class TestEventLog(TestCase):
    def setUp(self) -> None:
        self.event_log = EventLog()
        self.listener = Listener_Spy()
        self.second_listener = Listener_Spy()
        self.event_type = Event_Dummy
        self.event = self.event_type()

    def test_subscribe_listener_to_event__listener_subscribed(self):
        self.event_log.subscribe(listener=self.listener, event_type=self.event_type)

        self.assertDictEqual(self.event_log._subscribers, {self.event_type.__name__: [self.listener]})

    def test_subscribe_one_listener_instance_multiple_times_to_same_event__raise_exception(self):
        self.event_log.subscribe(listener=self.listener, event_type=self.event_type)

        self.assertRaises(EventLog.ListenerAlreadySubscribedToEvent,
                          self.event_log.subscribe,
                          self.listener, self.event_type)

    def test_subscribe_multiple_listener_instances_to_same_event__listeners_subscribed(self):
        self.event_log.subscribe(listener=self.listener, event_type=self.event_type)
        self.event_log.subscribe(listener=self.second_listener, event_type=self.event_type)

        self.assertDictEqual(self.event_log._subscribers,
                             {self.event_type.__name__: [self.listener, self.second_listener]})

    def test_subscribe_listener_to_multiple_events__listener_subscribed_to_events(self):
        second_event_type = Event_DummySecond

        self.event_log.subscribe(listener=self.listener, event_type=self.event_type)
        self.event_log.subscribe(listener=self.listener, event_type=second_event_type)

        self.assertDictEqual(self.event_log._subscribers,
                             {self.event_type.__name__: [self.listener], second_event_type.__name__: [self.listener]})

    def test_firing_events__call_subscribers(self):
        self.event_log.subscribe(listener=self.listener, event_type=self.event.__class__)
        self.event_log.subscribe(listener=self.second_listener, event_type=self.event.__class__)
        self.event_log.fire(event=self.event)

        self.assertTupleEqual(self.listener.call_stack[0], (self.listener.handle.__name__, self.event))
        self.assertTupleEqual(self.second_listener.call_stack[0], (self.second_listener.handle.__name__, self.event))

    def test_fire_event_with_no_subscribers__gracefully_end(self):
        self.event_log.fire(event=self.event)

        self.assertListEqual(self.listener.call_stack, [])
        self.assertListEqual(self.second_listener.call_stack, [])
