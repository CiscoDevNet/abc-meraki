# Asset Monitoring Dashboard 1.0
# Cisco Meraki IoT + Cisco Industrial Asset Vision
# MIT License, flopach / Cisco Systems 2021

import requests
import config
import pandas as pd
import influxdb_connect
import time
import meraki

dashboard = meraki.DashboardAPI("<add Meraki API Key>")

def get_switch_and_status_packets(orgs):
	"""
	Get all switch serials
	"""
	for org in orgs:
		networks = dashboard.organizations.getOrganizationNetworks(org["id"])

		for network in networks:
			devices=dashboard.networks.getNetworkDevices(network["id"])

			for device in devices:
				if "MS" in device["model"]:
					status_packets = dashboard.switch.getDeviceSwitchPortsStatusesPackets(device["serial"],timespan=86400)
					influxdb_connect.write_api.write(
						bucket=config.influx_bucket,
						org=config.influx_org,
						record=influxdb_connect.Point(status_packets))
						
def main():
	print("Getting Meraki information from Meraki Dashboard API")
	global switch_name_mapping
	orgs = dashboard.organizations.getOrganizations()
	while True:
		print("Polling now latest switch port data")
		get_switch_and_status_packets(orgs)		
		time.sleep(60) #poll every 10minutes