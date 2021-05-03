# Asset Monitoring Dashboard 1.0
# Cisco Meraki IoT + Cisco Industrial Asset Vision
# MIT License, flopach / Cisco Systems 2021

import requests
import config
import pandas as pd
import influxdb_connect
import time
import meraki

dashboard = meraki.DashboardAPI("")



def get_switch_and_status_packets(start):
	"""
	Get all switch serials
	"""
	orgs = dashboard.organizations.getOrganizations()
	for org in orgs:
		networks = dashboard.organizations.getOrganizationNetworks(org["id"])

		for network in networks:
			devices=dashboard.networks.getNetworkDevices(network["id"])

			for device in devices:
				if "MS" in device["model"]:
					packet_readings = dashboard.switch.getDeviceSwitchPortsStatusesPackets(device["serial"],timespan=86400)
					time.sleep(5)
					for port in packet_readings:
						device_id=device["serial"] + port["portId"] 
						for packet in port["packets"]:
							if start:
								packet['ts'] = pd.datetime.now()
								df = pd.DataFrame(packet)
								df = df.rename(columns={"ts":"ts",
									"value":"desc",
									"value":"total"})
								df = df.set_index("ts")
								influxdb_connect.write_api.write(
									bucket=config.influx_bucket,
									org=config.influx_org,
									record=df,
									data_frame_measurement_name=device_id)
							else: 
								
								ts = pd.datetime.now()
								influxdb_connect.write_api.write(
									bucket=config.influx_bucket,
									org=config.influx_org,
									record=influxdb_connect.Point(device_id)
									.field("serial_port",device_id)
									.field("packet_description",packet)
									.time(ts))




						
def main():
	print("Getting Meraki information from Meraki Dashboard API")


	# Gets at first the hisorical sensor data from the sensors in config.py
	print("Getting historical switch packet data")
	get_switch_and_status_packets(True)
		

	orgs = dashboard.organizations.getOrganizations()
	while True:
		print("Polling now latest switch port data")
		time.sleep(60) #poll every 10minutes
		get_switch_and_status_packets(False)
