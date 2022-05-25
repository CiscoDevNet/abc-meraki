import meraki

API_KEY = "INSERT YOUR API KEY HERE"
network_id = "YOUR_NETWORK_ID_HERE"

rules = [{'policy': 'deny', 'type': 'host', 'value': 'google.com'}, {'policy': 'deny', 'type': 'port', 'value': '23'}]

dashboard = meraki.DashboardAPI(API_KEY)

l7_firewall = dashboard.appliance.updateNetworkApplianceFirewallL7FirewallRules(
    network_id, 
    rules=rules
)

print(f"\nThe L7 Firewall have been updated.\n{l7_firewall}")