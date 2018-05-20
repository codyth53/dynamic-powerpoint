from datetime import datetime, timedelta
import urllib.request
import json


class CalendarEvent:
    def __init__(self, name, start, end, description, location, repeat_tag, config):
        self.name = name
        self.description = description
        self.location = location
        self.repeat_tag = repeat_tag
        self.hidden = False
        self.category = None

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

        self._process_description(description, config)

    def _process_description(self, description, config):
        lines = description.split('\n')

        for line in lines:
            if line.lower() == 'hidden':
                self.hidden = True
            if ':' in line:
                words = line.split(':')
                category_word = words[0]
                category = config.get_category(category_word)
                if category is not None:
                    self.category = category
                    break

    def __str__(self):
        return "{0} - {1} to {2}: {3}".format(self.name, self.start, self.end, self.repeat_tag)

    @staticmethod
    def clean_datetime(val):
        return val[:19]


class Calendar:
    def __init__(self, config):
        now = (config.get_date() - timedelta(days=1)).isoformat() + 'Z'
        eight_weeks_later = (config.get_date() + timedelta(days=56)).isoformat() + 'Z'
        print(now)

        url = "https://www.googleapis.com/calendar/v3/calendars/{0}/events?maxResults=100&singleEvents=true&timeMin={1}&timeMax={2}&key={3}"
        url = url.format(config.get_calendar_id(), now, eight_weeks_later, config.get_key())

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
            self.events.append(CalendarEvent(name, start, end, description, location, repeat, config))

        for event in self.events:
            print(event)

    def get_events(self, start=None, end=None):
        events = [x for x in self.events if
                  ((start is None or start is not None and x.start > start) and (start is None or start is not None and x.start < end)) or
                  ((end is None or end is not None and x.end > start) and (end is None or end is not None and x.end < end))]

        events.sort(key=lambda event: event.start)

        return events
