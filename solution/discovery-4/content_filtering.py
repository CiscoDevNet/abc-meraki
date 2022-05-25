import meraki

API_KEY = "INSERT YOUR API KEY HERE"
network_id = "YOUR_NETWORK_ID_HERE"

allowedUrlPatterns=["http://www.example.org", "http://help.com"]
blockedUrlPatterns=["http://www.games.com", "http://www.betting.com"]
blockedUrlCategories=["meraki:contentFiltering/category/1",      "meraki:contentFiltering/category/7"]
urlCategoryListSize='topSites'

dashboard = meraki.DashboardAPI(API_KEY)

content_filter = dashboard.appliance.updateNetworkApplianceContentFiltering(
    network_id,
    allowedUrlPatterns=allowedUrlPatterns,
    blockedUrlPatterns=blockedUrlPatterns,
    blockedUrlCategories=blockedUrlCategories,
    urlCategoryListSize=urlCategoryListSize
    )

print(f'\nContent filtering rules have been configured.\n{content_filter}')