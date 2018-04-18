import json


class DpConfig:
    def __init__(self, filepath):
        try:
            config_file = open(filepath, 'r')
            config_contents = config_file.read()
            config_file.close()
        except:
            raise Exception("Unable to read file")

        config = json.loads(config_contents)

        self._google_calendar_id = config['calendar-id']
        self._key = config['key']

    def get_calendar_id(self):
        return self._google_calendar_id

    def get_key(self):
        return self._key
