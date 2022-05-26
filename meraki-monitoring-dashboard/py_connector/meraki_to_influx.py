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
	try: 
		orgs = dashboard.organizations.getOrganizations()
		for org in orgs:
			if "HTD" in org["name"]:
				networks = dashboard.organizations.getOrganizationNetworks(org["id"])

				for network in networks:
					devices=dashboard.networks.getNetworkDevices(network["id"])

					for device in devices:
						if "MS" in device["model"]:
							packet_readings = dashboard.switch.getDeviceSwitchPortsStatusesPackets(device["serial"],timespan=10)
							for port in packet_readings:
								device_id=device["serial"] + port["portId"] 
								for packet in port["packets"]:
									device_id=device["serial"] + port["portId"] + packet['desc']
									if start:
										df_packet = {}
										df_packet['switch'] = device["serial"]
										df_packet['port'] = port["portId"]
										df_packet['desc'] = packet['desc']
										df_packet['total'] = packet['total']
										df_packet['ts'] = pd.datetime.now()
										df = pd.DataFrame(df_packet)
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
											.field("switch",device["serial"])
											.field("port",port["portId"])
											.field("total",packet['total'])
											.field("desc",packet['desc'])
											.time(ts))
	except Exception as e:
		print(e)



						
def main():
	print("Getting Meraki information from Meraki Dashboard API")


	# Gets at first the hisorical sensor data from the sensors in config.py
	print("Getting historical switch packet data")
	get_switch_and_status_packets(True)
		

	orgs = dashboard.organizations.getOrganizations()
	while True:
		print("Polling now latest switch port data")
		time.sleep(60) #poll every 1 minutes
		get_switch_and_status_packets(False)
