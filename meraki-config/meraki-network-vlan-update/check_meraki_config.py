import unittest

from meraki_network_vlan_provision import *

class check_meraki_config_test(unittest.TestCase):
    """test module to test config read in meraki_network_vlan_provision.py` """

    def test_column_names(self):
        config_columns = get_config()
        config_columns = list(config_columns[0].keys())
        self.assertEqual(["Network_Name","VLAN_subnet","Number_VLANS"], \
            config_columns, "Config Columns correct")

    def test_values_exist(self):
        configs = get_config()

        for index, config in enumerate(configs, 1):
            if index > 0:
                self.assertTrue(type(config["Network_Name"]) is str, f"Network {index} checks")
                self.assertTrue(type(config["VLAN_subnet"]) is str and len(config["VLAN_subnet"].split(".")) == 2, f"subnet {index} checks")
                self.assertTrue(type(config["Number_VLANS"]) is str and len(config["Number_VLANS"]) > 0, f"Num vlan {index} checks")
            

if __name__ == '__main__':
    unittest.main()