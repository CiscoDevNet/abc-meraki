import unittest

from meraki_network_vlan_provision import *

class check_for_same_name_networks_test(unittest.TestCase):
    """test module to test config will be applied against an existing network in meraki_network_vlan_provision.py` """

    def test_same_name_network(self):
        config = get_config()

        orgs = dashboard.organizations.getOrganizations()
        found_networks = []
        for org in orgs:  
            network_actions=[]
            # Get the new network ID so we can add the devices
            networks = dashboard.organizations.getOrganizationNetworks(org["id"])
            
            header = True

            for row in config:
                if header:
                    print(f'Column names are {", ".join(row)}')
                    header = False

                
                for network in networks:
                    if network["name"] == row["Network_Name"]:
                        print(f"{row['Network_Name']} found!")
                        found_networks.append(network["name"])



        self.assertTrue(len(found_networks) >= len(config)-1)

if __name__ == '__main__':
    unittest.main()