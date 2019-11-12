# Setup InfluxDB

[Influx Docker Image](https://hub.docker.com/_/influxdb)

[Chronograph Docker Image](https://hub.docker.com/_/chronograf)

Some Config Info from this [Medium post](https://medium.com/@sidstuart/installing-telegraph-influx-cronograf-kapacitor-in-containers-f26b8022ea87)


Init DB
```
docker run --rm \
      -e INFLUXDB_DB=db0 -e INFLUXDB_HTTP_AUTH_ENABLED=true \
      -e INFLUXDB_ADMIN_USER=<admin_user> -e INFLUXDB_ADMIN_PASSWORD=<password> \
      -e INFLUXDB_USER=<readonly_user> -e INFLUXDB_USER_PASSWORD=<password> \
      -v ~/Developer/influxData:/var/lib/influxdb \
      influxdb:1.7.7-alpine /init-influxdb.sh
```
Start DB as daemon (to connect and create users / check settings settings)
```
docker run --rm -v ~/Developer/influxData:/var/lib/influxdb \
    --name=influxdb -d -p 8086:8086 influxdb:1.7.7-alpine
```
Connect to console from another container (saves on installing influx client on host)

```
docker run --rm --link=influxdb -it influxdb:1.7.7-alpine influx -host influxdb
```
> show users
> show databases


Generate the default configuration file:

```docker run --rm influxdb:1.7.7-alpine influxd config > influxdb.conf```

Modify the default configuration as necessary.

```line #64: auth-enabled = true```

stop / delete running container & create docker network

```docker network create influxdb```

Start new daemon with local config
```
docker run \
    -v ~/Developer/influxData:/var/lib/influxdb -v $PWD/influxdb.conf:/etc/influxdb/influxdb.conf:ro \
    --net=influxdb \
    --restart unless-stopped --name=influxdb -d -p 5454:8086 influxdb:1.7.7-alpine -config /etc/influxdb/influxdb.conf
```   
Connect to console from another container with authentication (or auth in influx console)
```
docker run --rm --link=influxdb --net=influxdb -it influxdb:1.7.7-alpine influx -precision=rfc3339 -database="db0" -host influxdb -username <admin_user> -password <password>
```
run these commands
```
> CREATE RETENTION POLICY "a_year" ON db0 DURATION 52w REPLICATION 1 DEFAULT
> CREATE USER "<user>" WITH PASSWORD '<password>' WITH ALL PRIVILEGES
```

### Setup / Run Chronograph 
#### (depreciated - not secure under planned setup)

Start Chronograph with mounted local data
```
docker run -d -p 8888:8888 --net=influxdb \
      -v ~/Developer/influxData/_chronograph:/var/lib/chronograf \
      --restart unless-stopped --name=chronograph --link=influxdb \
      chronograf:alpine --influxdb-url=http://influxdb:8086
```      

## Start init Grafana  
```
docker run \
  --rm \
  -p 3030:3000 \
  --name=grafana \
  --net=influxdb \
  -v ~/Developer/influxData/_grafana:/var/lib/grafana \
  -e "GF_SERVER_ROOT_URL=http://grafana.kokaruk.com" \
  -e "GF_SECURITY_ADMIN_PASSWORD=<password>" \
  grafana/grafana
```
## Start Grafana Service
```  
docker run \
  -d --restart unless-stopped \
  -p 127.0.0.1:3030:3000 \
  --name=grafana \
  --net=influxdb \
  -v $PWD/grafana.ini:/etc/grafana/grafana.ini \
  -v ~/Developer/influxData/_grafana:/var/lib/grafana \
  grafana/grafana
```  
  
  
  After final setup & confirm that server is running switch to Google OAuth (and disable password)
  as per [Grafana Doc](https://grafana.com/docs/auth/google/)