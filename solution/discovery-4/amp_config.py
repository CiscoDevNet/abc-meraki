import meraki

API_KEY = "INSERT YOUR API KEY HERE"
network_id = "YOUR_NETWORK_ID_HERE"

mode = 'enabled'
allowedUrls = [{'url': 'www.cisco.com', 'comment': 'test'}, {'url': 'www.google.com', 'comment': 'allow google.com'}]
allowedFiles = [{'sha256': 'e82c5f7d75004727e1f3b94426b9a11c8bc4c312a9170ac9a73abace40aef503', 'comment': 'allow ZIP file'}]

dashboard = meraki.DashboardAPI(API_KEY)

amp_config = dashboard.appliance.updateNetworkApplianceSecurityMalware(
    network_id, mode,
    allowedUrls=allowedUrls,
    allowedFiles=allowedFiles
)

print(f"\nThe AMP configuration has been updated.\n{amp_config}")