#!/usr/bin/env python3
"""
* Authors : Patrick Jacob, Dzmitry Kakaruk,
*
* Version info 1.0.
*
* This program is created for Assignment 1 of Programming Internet of Things -  Course Master of IT - RMIT University.
* This code has parts which are inspired by the course material of  - Programming Internet of Things  - RMIT University.
*
* The purpose of the Program is to read the senseHat Data (Temperature, Humidity and Pressure)
* of a RaspberryPi and send to a Database and PushBullet.
* For more information please see: https://github.com/kokaruk/IOT-A1.
* This is the main class and serves as starting point of the program.
*
* Copyright notice - All copyrights belong to Dzmitry Kakaruk, Patrick Jacob - August 2018
"""

# import os
import time
# import json
#
# from datetime import datetime, timedelta
# from json import JSONDecodeError

from sense_hat import SenseHat
from conf.config import SenseHatReadings, logger, RUNS_PER_MINUTE, SLEEP_TIME
from gpiozero import CPUTemperature
from threading import Thread
from services.influx_db_proxy import InfluxDBProxy
from services.saytime import main as say_time

sense = SenseHat()


def main():
    logger.info("start execution")
    Thread(target=say_time).start()
    write_to_db()


def read_sensor() -> SenseHatReadings:
    return SenseHatReadings(temperature=sense.get_temperature_from_pressure(),
                            cpu_temp=CPUTemperature().temperature,
                            pressure=sense.get_pressure(),
                            humidity=sense.get_humidity())


def write_to_db():
    database_accessor: InfluxDBProxy = InfluxDBProxy()  # init database accessor
    for i in range(RUNS_PER_MINUTE):
        sense_hat_readings: SenseHatReadings = read_sensor()
        database_accessor.write_sh_readings(sense_hat_readings)
        time.sleep(SLEEP_TIME)


# calling main and starting the program
if __name__ == '__main__':
    main()
