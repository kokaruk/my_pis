"""
* Authors : Patrick Jacob, Dzmitry Kakaruk
*
* Version info 1.0.
*
* This program is created for Assignment 1 of Programming Internet of Things -  Course Master of IT - RMIT University.
* This code has parts which are inspired by the course material of  - Programming Internet of Things  - RMIT University.
*
* The purpose of the Program is to read the senseHat Data (Temperature, Humidity and Pressure)
* of a RaspberryPi and send to a Database and PushBullet.
* For more information please see: https://github.com/kokaruk/IOT-A1
* This Class is responsible for the passing of SenseHat Data to the Database
*
* Copyright notice - All copyrights belong to Dzmitry Kakaruk, Patrick Jacob - August 2018
"""

import datetime
import json
import os

from influxdb import InfluxDBClient
from influxdb import exceptions

from conf.config import DIR_PATH, SenseHatReadings, logger


class InfluxDBProxy:
    CONF_FILE = os.path.join(DIR_PATH, '../conf/influx_connect.json')

    @staticmethod
    def read_config_json() -> dict:
        try:
            with open(InfluxDBProxy.CONF_FILE, "r") as connect_file:
                return json.load(connect_file)
        except (FileNotFoundError, IOError):
            logger.critical(f"{InfluxDBProxy.CONF_FILE} not found")

    def __init__(self, host='192.168.50.75', port=5454):
        connect = InfluxDBProxy.read_config_json()
        self._username = connect["user"]
        self._client = InfluxDBClient(host=host,
                                      port=port,
                                      username=connect["user"],
                                      password=connect["password"],
                                      database=connect["database"])

    def write_sh_readings(self, sense_hat_readings: SenseHatReadings) -> None:
        """
        following this tutorial as basis: https://www.circuits.dk/datalogger-example-using-sense-hat-influxdb-grafana/
        heavily modified
        writing readings
        """
        try:
            # write measurements of DB
            write_data = [
                {
                    "measurement": "SenseHatReadings",
                    "tags": {"user": self._username},
                    "time": datetime.datetime.utcnow().isoformat(),
                    "fields": {
                        "temperature": float(sense_hat_readings.temperature),
                        "cpu_temperature": float(sense_hat_readings.cpu_temp),
                        "humidity": float(sense_hat_readings.humidity),
                        "pressure": float(sense_hat_readings.pressure)
                    }
                }
            ]

            result = self._client.write_points(write_data)

            # log if unsuccessful event
            if not result:
                logger.error(f"SenseHat to influxDatabase write : {result}")
        except exceptions.InfluxDBClientError as err:
            logger.error(f"Error writing to the database: {err}")
