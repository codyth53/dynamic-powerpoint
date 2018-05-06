from datetime import datetime
import urllib.request
import json


class CalendarEvent:
    def __init__(self, name, start, end, description, location, repeat_tag):
        self.name = name
        self.description = description
        self.location = location
        self.repeat_tag = repeat_tag

        if 'date' in start:
            self.start = datetime.strptime(start['date'], '%Y-%m-%d')
        elif 'dateTime' in start:
            val = self.clean_datetime(start['dateTime'])
            self.start = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S')
        else:
            self.start = None

        if 'date' in end:
            self.end = datetime.strptime(end['date'], '%Y-%m-%d')
        elif 'dateTime' in end:
            val = self.clean_datetime(end['dateTime'])
            self.end = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S')
        else:
            self.end = None

    def __str__(self):
        return "{0} - {1} to {2}".format(self.name, self.start, self.end)

    @staticmethod
    def clean_datetime(val):
        return val[:19]


class Calendar:
    def __init__(self, config):
        now = datetime.utcnow().isoformat() + 'Z'
        print(now)

        url = "https://www.googleapis.com/calendar/v3/calendars/{0}/events?maxResults=20&singleEvents=true&timeMin={1}&key={2}"
        url = url.format(config.get_calendar_id(), now, config.get_key())

        print("requesting {0}".format(url))
        get_result = urllib.request.urlopen(url)

        events = json.loads(get_result.read().decode('utf-8'))

        self.events = []

        for item in events['items']:
            name = item['summary']
            start = item['start']
            end = item['end']
            description = item.get('description', '')
            location = item.get('location')
            repeat = item.get('recurringEventId')
            self.events.append(CalendarEvent(name, start, end, description, location, repeat))

        for event in self.events:
            print(event)
