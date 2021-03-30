# Asset Monitoring Dashboard 1.0
# Cisco Meraki IoT + Cisco Industrial Asset Vision
# MIT License, flopach / Cisco Systems 2021

# ================================= #
#          GLOBAL Settings          #
# ================================= #
# Configure before building up and running docker-compose
# Select 1 to enable or 0 to DISable data collection for Meraki MT sensors or Industrial Asset Vision
# ================================= #
### DO NOT EDIT! ###
# static config data for InfluxDB 
# InfluxDB
influx_token = "meraki_token123"
influx_org = "meraki_organization"
influx_bucket = "meraki_bucket"
influx_url = "http://influxdb:8086"