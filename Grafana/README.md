## Setup host influxDB Dockerfile

Generate the default configuration file:

docker run --rm influxdb influxd config > influxdb.c

Modify the default configuration, and build image

docker build --build-arg INFLUXDB_ADMIN_PASSWORD=pass --build-arg -t influx:local .

Init Database
docker run --rm -v ~/Developer/influxData:/var/lib/influxdb -p 8086:8086 influx:local -config /etc/influxdb/influxdb.conf 

Start Daemon
docker run --name=influxdb -v ~/Developer/influxData:/var/lib/influxdb -d -p 8086:8086 influx:local

Connect to console
docker run --rm --link=influxdb -it influx:local influx -host influxdb

CREATE RETENTION POLICY "a_year" ON db0 DURATION 52w REPLICATION 1 DEFAULT

## Setup grafana docker file

