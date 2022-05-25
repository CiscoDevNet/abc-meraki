import requests

api_key = "<INSERT-API-KEY-HERE>"
serial_number = "<INSERT-SERIAL-NUMBER-HERE>"
url = "https://api.meraki.com/api/v1/devices/" + serial_number + "/switch/routing/interfaces"

payload = '''{
    "name": "Meraki bootcamp SVI Python",
    "subnet": "192.168.4.0/24",
    "interfaceIp": "192.168.4.2",
    "vlanId": 20,
    "multicastRouting": "disabled"
    }'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text)