import meraki

API_KEY = "<INSERT YOUR API KEY HERE>"
network_id = "<YOUR_NETWORK_ID_HERE>"

vlan = 100
protocol = 'TCP'
srcPort = 100
dstPort = 200
dscp = 0

dashboard = meraki.DashboardAPI(API_KEY)

qos_config = dashboard.switch.createNetworkSwitchQosRule(
    network_id, vlan,
    protocol=protocol,
    srcPort=srcPort,
    dstPort=dstPort,
    dscp=dscp
)

print(f"\nThe QoS configuration has been created.\n{qos_config}")