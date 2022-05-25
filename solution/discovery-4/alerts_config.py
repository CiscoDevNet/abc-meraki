import meraki

API_KEY = "INSERT YOUR API KEY HERE"
network_id = "YOUR_NETWORK_ID_HERE"

defaultDestinations = {'emails': ['name@yourcompany.com'], 'allAdmins': False, 'snmp': True}
alerts = [{'type': 'gatewayDown', 'enabled': True, 'alertDestinations': {'emails': ['name@yourcompany.com'], 'allAdmins': False, 'snmp': False}, 'filters': {'timeout': 60}}]

dashboard = meraki.DashboardAPI(API_KEY)

alerts_config = dashboard.networks.updateNetworkAlertsSettings(
    network_id,
    defaultDestinations=defaultDestinations,
    alerts=alerts
)

print(f'\nAlerts have been configured.\n{alerts_config}')