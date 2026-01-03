import os
import time
import math
import random
import requests

INFLUX_URL = os.getenv("INFLUX_URL", "http://localhost:8086")
ORG = os.getenv("INFLUX_ORG", "ee2510")
BUCKET = os.getenv("INFLUX_BUCKET", "iot_bucket")
TOKEN = os.getenv("INFLUX_TOKEN")
DEVICE_ID = os.getenv("DEVICE_ID", "sim01")
INTERVAL_SEC = float(os.getenv("INTERVAL_SEC", "5"))

if not TOKEN:
    raise SystemExit("INFLUX_TOKEN отсутствует. Проверь .env и переменные окружения.")

write_url = f"{INFLUX_URL}/api/v2/write"
params = {"org": ORG, "bucket": BUCKET, "precision": "s"}
headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "text/plain; charset=utf-8"
}

t = 0.0
print("Producer started. Writing telemetry to InfluxDB...")

while True:
    temperature = 22.0 + 3.0 * math.sin(t / 30.0) + random.uniform(-0.2, 0.2)
    humidity = 40.0 + 8.0 * math.sin(t / 45.0) + random.uniform(-0.5, 0.5)

    line = (
        f"telemetry,device_id={DEVICE_ID} "
        f"temperature_c={temperature:.2f},humidity_pct={humidity:.2f}"
    )

    r = requests.post(write_url, params=params, headers=headers, data=line, timeout=10)
    if r.status_code >= 300:
        print("Write failed:", r.status_code, r.text)
    else:
        print("OK:", line)

    t += INTERVAL_SEC
    time.sleep(INTERVAL_SEC)
