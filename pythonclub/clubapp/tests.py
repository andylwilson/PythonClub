from django.test import TestCase
from .models import Meeting, Minutes, Resource, Event

# Create your tests here.

# Tests for models
class MeetingTest(TestCase):
    def test_string(self):
        meeting=Meeting(meetingtitle='May Study Meetup')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MinutesTest(TestCase):
    def test_string(self):
        agenda=Minutes(minutes='Our monthly study session about Python')
        self.assertEqual(str(agenda), agenda.minutes)

    def test_table(self):
        self.assertEqual(str(Minutes._meta.db_table), 'minutes')

class ResourceTest(TestCase):
    def test_string(self):
        resource=Resource(resourcename='YouTube Tutorial')
        self.assertEqual(str(resource), resource.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        event=Event(eventtitle='Study at Central')
        self.assertEqual(str(event), event.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')