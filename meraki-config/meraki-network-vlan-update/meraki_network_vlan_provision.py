import json
import random
import sys
import os
import getopt
from action_batches import create_action_batch, check_until_completed
from time import sleep
import csv
import meraki

dashboard = meraki.DashboardAPI()

def check_batch_completion(org,batch_id):
    counter = 0
    while True:
        batch = dashboard.organizations.getOrganizationActionBatch(org,batch_id)
        if batch['status']['completed'] and not batch['status']['failed']:
            print('Action batch ' +  batch_id +  ' completed!')
            break
        elif batch['status']['failed']:
            print(batch)
            break
        else:
            print('Action batch ' +  batch_id + 'processing... ' + str(99 - counter) + ' iterations')
            sleep(1)
        counter += 1

def get_config():
    with open('meraki_config.csv', mode='r') as csv_file:
        config = csv.DictReader(csv_file)
        config = list(config)
        print(config)
        return config
        

def find_network_and_assign_vlan():
    # Get the new network ID so we can add the devices
    orgs = dashboard.organizations.getOrganizations()
    config = get_config()

    for org in orgs:  
        # Get the new network ID so we can add the devices
        networks = dashboard.organizations.getOrganizationNetworks(org["id"])

        header = True
        network_found = False

        for row in config:
            if header:
                print(f'Column names are {", ".join(row)}')
                header = False

            for network in networks:
                if network["name"] == row["Network_Name"]:
                    network_found = True
                    network = network["id"] 
                    if int(row["Number_VLANS"]) > 0:
                        dashboard.appliance.updateNetworkApplianceVlansSettings(network,vlansEnabled=True)
                        network_vlan_actions = []
                        for number in range(int(row["Number_VLANS"])):
                            network_vlan_actions.append({
                                "resource": f"/networks/{network}/vlans",
                                "operation": "create",
                                "body": {
                                    "id": number+2,
                                    "name": f"VLAN {number+2}",
                                    "applianceIp": f"{row['VLAN_subnet']}.{number+2}.1",
                                    "subnet": f"{row['VLAN_subnet']}.{number+2}.0/24"
                                }
                            })

                        batch = dashboard.organizations.createOrganizationActionBatch(org["id"],network_vlan_actions,confirmed=True,synchronous=False)
                        check_batch_completion(org["id"],batch["id"])
            
            if not network_found:
                raise ValueError(f"No network with name {row['Network_Name']} found!")

if __name__ == "__main__":
    find_network_and_assign_vlan()



