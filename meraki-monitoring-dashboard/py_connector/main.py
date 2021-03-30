# Asset Monitoring Dashboard 1.0
# Cisco Meraki IoT + Cisco Industrial Asset Vision
# MIT License, flopach / Cisco Systems 2021
import meraki_to_influx
import config
import time
from threading import Thread

if __name__ == "__main__":
    print("Starting py_connector")
    time.sleep(60) #wait for influxdb

    thread_meraki = Thread(target=meraki_to_influx.main)
    thread_meraki.start()