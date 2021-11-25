'''
Create a new network and organization

This script asks for the API key during the runtime,
and then creates an Organization and Network under that
API key.
The script requires meraki Python library, please install
it with pip if you don't yet have it in your system.
'''

import meraki

ORG_NAME = "My Test Meraki Organization"
NETWORK_NAME = "My Test Meraki Network"
PRODUCT_TYPES = ['appliance']

api_key = input("Please enter your API key: ")
dashboard = meraki.DashboardAPI(api_key)

response = dashboard.organizations.createOrganization(ORG_NAME)
org_id = response["id"]

response = dashboard.organizations.createOrganizationNetwork(org_id, NETWORK_NAME, PRODUCT_TYPES)
network_id = response["id"]

info_message = f"New organization ID: {org_id}\nNew network ID: {network_id}"
print(info_message)

with open("./id_info.txt", "w") as file:
    file.write(info_message)
