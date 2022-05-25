import meraki

API_KEY = '<ADD_YOUR_API_KEY_HERE>'
dashboard = meraki.DashboardAPI(API_KEY)
serial = '<ADD_YOUR_SERIAL_NUMBER_HERE>'

response = dashboard.devices.updateDevice(
    serial, 
    tags=['meraki_bootcamp']

)

print(response)
