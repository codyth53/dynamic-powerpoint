from dynamic_powerpoint.calendar_utils import Calendar
from dynamic_powerpoint.settings_parser import DpConfig


class PowerpointGenerator:
    def __init__(self, config: DpConfig, calendar: Calendar):
        self.config = config
        self.calendar = calendar
