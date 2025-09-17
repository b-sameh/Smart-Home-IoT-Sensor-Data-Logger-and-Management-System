#!/usr/bin/env python3
import os, time, random

sensor = os.getenv("SENSOR_TYPE", "Unknown")
while True:
    value = round(random.uniform(20.0, 30.0), 2)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} | {sensor}: {value}°C", flush=True)
    time.sleep(2)


