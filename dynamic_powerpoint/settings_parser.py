import json
from datetime import datetime


class ConfigCategory:
    def __init__(self, dict):
        self.name = dict['name']

        if 'color' in dict:
            self.color = dict['color']

        try:
            self.hidden = bool(dict['hidden'])
        except:
            self.hidden = False

        try:
            self.transparency = float(dict['transparency'])
        except:
            self.transparency = None


class EightWeekConfig:
    def __init__(self, dict):
        if 'month-one-color' in dict:
            self.month_one_color = dict['month-one-color']
        else:
            self.month_one_color = "FFFFFF"

        if 'month-two-color' in dict:
            self.month_two_color = dict['month-two-color']
        else:
            self.month_two_color = "FFFFFF"


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

        self.categories = {}
        category_input = config['categories'] if 'categories' in config else []
        self._process_categories(category_input)

        eight_week_config = config['eight-week'] if 'eight-week' in config else {}
        self.eight_week = EightWeekConfig(eight_week_config)

    def _process_categories(self, category_input):
        for category in category_input:
            category_item = ConfigCategory(category)
            self.categories[category_item.name] = category_item

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

    def get_category(self, category):
        if category in self.categories.keys():
            return self.categories[category]
        else:
            return None
