import argparse
from .settings_parser import DpConfig
from .calendar_utils import Calendar
from .powerpoint_generator.powerpoint_generator import PowerpointGenerator
from .powerpoint_generator.main_generator import generate_powerpoint


def run():
    parser = argparse.ArgumentParser(description="Generate a PowerPoint based on Google Calendar events.")
    parser.add_argument('config_path', metavar='C', type=str, help='The path to the config file')
    parser.add_argument('date', metavar='D', type=str, help='Start date to generate events')

    args = parser.parse_args()

    config = DpConfig(args.config_path, args.date)

    calendar = Calendar(config)

    powerpoint_generator = PowerpointGenerator(config, calendar)

    generate_powerpoint(powerpoint_generator)

