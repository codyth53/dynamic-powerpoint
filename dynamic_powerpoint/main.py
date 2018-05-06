import argparse
from .settings_parser import DpConfig
from.calendar_utils import Calendar


def run():
    parser = argparse.ArgumentParser(description="Generate a PowerPoint based on Google Calendar events.")
    parser.add_argument('config_path', metavar='C', type=str, help='The path to the config file')
    parser.add_argument('date', metavar='D', type=str, help='Start date to generate events', required=False)

    args = parser.parse_args()

    config = DpConfig(args.config_path, args.date)

    calendar = Calendar(config)
