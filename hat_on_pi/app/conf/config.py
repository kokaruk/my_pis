"""
* Authors : Patrick Jacob, Dzmitry Kakaruk
*
* Version info 1.0.
*
* This program is created for Assignment 1 of Programming Internet of Things -  Course Master of IT - RMIT University.
* This code has parts which are inspired by the course material of  - Programming Internet of Things  - RMIT University.
*
* The purpose of this module is a unified storage of all constant values
*
* Copyright notice - All copyrights belong to Dzmitry Kakaruk, Patrick Jacob - August 2018
"""
import configparser
import os
import logging
from logging.handlers import RotatingFileHandler
import sys
from dataclasses import dataclass

# ******************************
# all modules constants and classes
# ******************************
DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # getting current file absolute path, required for cron jobs
LOG_PATH = os.path.join(DIR_PATH, '../logs')

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
file_handler = RotatingFileHandler(f'{LOG_PATH}/weather_system_errors.log', maxBytes=10240,
                                   backupCount=10)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

logger = logging.getLogger("grafana")
logger.addHandler(file_handler)

config = configparser.ConfigParser()  # reading config from ini file
config_path = os.path.join(DIR_PATH, './config.ini')
config.read(config_path)

# send notification when passing this temp threshold
try:
    LOWER_TEMPERATURE_THRESHOLD = float(config['Globals']['lower_temperature_threshold'])
    UPPER_TEMPERATURE_THRESHOLD = float(config['Globals']['upper_temperature_threshold'])
except KeyError:
    logger.critical("can't read config file")
    sys.exit(1)


@dataclass
class SenseHatReadings:
    """
    data class for storing values from sense hat
    """
    temperature: float
    cpu_temp: float
    humidity: float
    pressure: float

    @staticmethod
    def get_reading_as_string(value: float, unit: str) -> str:
        units_strings = {
            'temperature': '˚C',
            'cpu_temp:': '˚C',
            'humidity': '%',
            'pressure': 'mbar'
        }
        return f"{round(value, 2)}{units_strings[unit]}"


# ******************************
# MAIN MODULE CONSTANTS
# *******************************
try:
    RUNS_PER_MINUTE = int(config['Globals']['runs_per_minute'])
    MESSAGE_HOLD = float(config['Globals']['message_hold'])
except KeyError:
    logger.critical("can't read config file")
    sys.exit(1)
SLEEP_TIME: int = int(60 / RUNS_PER_MINUTE)  # 60 seconds in a minute
MESSENGER_FLAG_PATH = os.path.join(DIR_PATH, 'data/msg_flags.json')

DATE_FORMAT = '%d/%m/%Y %H:%M:%S'
