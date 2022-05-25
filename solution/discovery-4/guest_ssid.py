import meraki

API_KEY = "INSERT YOUR API KEY HERE"
network_id = "YOUR_NETWORK_ID_HERE"

name = 'Guest configured'
number = 2
enabled = True
authMode = 'open'
ipAssignmentMode = 'NAT mode'
perClientBandwidthLimitUp = 100
perClientBandwidthLimitDown = 500
perSsidBandwidthLimitDown = 2000

dashboard = meraki.DashboardAPI(API_KEY)

ssid = dashboard.wireless.updateNetworkWirelessSsid(network_id, number,
    name=name,
    enabled=enabled,
    authMode=authMode,
    perClientBandwidthLimitDown=perClientBandwidthLimitDown,
    perClientBandwidthLimitUp=perClientBandwidthLimitUp,
    perSsidBandwidthLimitDown=perSsidBandwidthLimitDown,
    ipAssignmentMode=ipAssignmentMode
    )

print(f'\Wireless Guest Access has been configured.\n{ssid}')