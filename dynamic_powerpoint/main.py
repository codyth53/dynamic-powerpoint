import argparse
from .settings_parser import DpConfig
from .calendar_utils import Calendar
from .powerpoint_generator.powerpoint_generator import PowerpointGenerator
from .powerpoint_generator.main_generator import generate_powerpoint
import logging


logger = logging.getLogger('dynamic_powerpoint')
consoleHandler = logging.StreamHandler()
logger.addHandler(consoleHandler)


def run():
    parser = argparse.ArgumentParser(description="Generate a PowerPoint based on Google Calendar events.")
    parser.add_argument('config_path', metavar='C', type=str, help='The path to the config file')
    parser.add_argument('date', metavar='D', type=str, help='Start date to generate events')
    parser.add_argument('-l', '--logging', type=int, help='Log level for debugging', required=False, choices=[1, 2])

    args = parser.parse_args()

    if 'logging' in args:
        if args.logging == 1:
            logger.setLevel(logging.INFO)
        elif args.logging == 2:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.WARN)
    else:
        logger.setLevel(logging.WARN)

    config = DpConfig(args.config_path, args.date)

    calendar = Calendar(config)

    powerpoint_generator = PowerpointGenerator(config, calendar)

    generate_powerpoint(powerpoint_generator)

