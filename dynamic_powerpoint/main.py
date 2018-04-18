import argparse
from .settings_parser import DpConfig
from.calendar_utils import Calendar


def run():
    parser = argparse.ArgumentParser(description="Generate a PowerPoint based on Google Calendar events.")
    parser.add_argument('config_path', metavar='C', type=str, help='The path to the config file')

    args = parser.parse_args()

    config = DpConfig(args.config_path)

    calendar = Calendar(config)
