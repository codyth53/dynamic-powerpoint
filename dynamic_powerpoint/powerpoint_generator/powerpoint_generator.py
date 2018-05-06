from pptx import Presentation
from dynamic_powerpoint.calendar_utils import Calendar
from dynamic_powerpoint.settings_parser import DpConfig


class PowerpointGenerator:
    def __init__(self, config: DpConfig, calendar: Calendar):
        self.config = config
        self.calendar = calendar


def generate_powerpoint(pg: PowerpointGenerator):
    pptx = Presentation(pg.config.get_template_path())

    print(pptx)