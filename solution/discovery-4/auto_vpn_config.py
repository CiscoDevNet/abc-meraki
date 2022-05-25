import meraki

API_KEY = "<INSERT YOUR API KEY HERE>"
network_id = "<INSERT YOUR NETWORK ID HERE>"

mode = 'spoke'
hubs= [{'hubId': 'N_622059698530563433', 'useDefaultRoute': False}, {'hubId': 'N_622059698530563431', 'useDefaultRoute': False}]
subnets= [{'localSubnet': '192.168.128.0/24', 'useVpn': True}]

dashboard = meraki.DashboardAPI(API_KEY)

auto_vpn = dashboard.appliance.updateNetworkApplianceVpnSiteToSiteVpn(
    network_id,
    mode,
    hubs=hubs,
    subnets=subnets
)

print(f'\nSite-to-site VPN has been updated.\n{auto_vpn}')