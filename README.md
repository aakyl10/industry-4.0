\# IoT Sensor Data Collection \& Visualization (HTTP → InfluxDB → Grafana)



\## Overview

This project simulates an IoT sensor device and sends telemetry (temperature, humidity) to InfluxDB via HTTP.

Grafana is used to visualize the data on a dashboard.



\## Stack

\- Docker Compose

\- InfluxDB 2.x (time-series database)

\- Grafana (dashboard/visualization)

\- Python producer (simulated sensor)



\## Architecture

Producer (Python) → HTTP write → InfluxDB (bucket: iot\_bucket, org: st2302) → Grafana dashboard



\## Run

1\) Create `.env` in project root (example keys):

\- INFLUX\_TOKEN=...

\- INFLUX\_ORG=st2302

\- INFLUX\_BUCKET=iot\_bucket

\- INFLUX\_USERNAME=admin

\- INFLUX\_PASSWORD=...

\- GRAFANA\_ADMIN\_USER=admin

\- GRAFANA\_ADMIN\_PASSWORD=...

\- DEVICE\_ID=sim01

\- INTERVAL\_SEC=5



2\) Start containers:

```bash

docker compose up -d



