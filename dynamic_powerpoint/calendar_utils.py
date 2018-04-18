import datetime
import urllib.request
import json


class CalendarEvent:
    pass


class Calendar:
    def __init__(self, config):
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print(now)

        url = "https://www.googleapis.com/calendar/v3/calendars/{0}/events?maxResults=20&singleEvents=true&timeMin={1}&key={2}"
        url = url.format(config.get_calendar_id(), now, config.get_key())

        print("requesting {0}".format(url))
        get_result = urllib.request.urlopen(url)

        events = json.loads(get_result.read().decode('utf-8'))

        print(events)
