import json
from datetime import datetime


class DpConfig:
    def __init__(self, filepath, date):
        try:
            config_file = open(filepath, 'r')
            config_contents = config_file.read()
            config_file.close()
        except:
            raise Exception("Unable to read file")

        config = json.loads(config_contents)

        self._google_calendar_id = config['calendar-id']
        self._key = config['key']
        self._template_path = config['template-path']
        self._save_path = config['save-path']

        if date:
            self._date = datetime.strptime(date, '%m-%d-%Y')
        else:
            self._date = datetime.today()

    def get_calendar_id(self):
        return self._google_calendar_id

    def get_key(self):
        return self._key

    def get_template_path(self):
        return self._template_path

    def get_save_path(self):
        return self._save_path

    def get_date(self) -> datetime:
        return self._date
