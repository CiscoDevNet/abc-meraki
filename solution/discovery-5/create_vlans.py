import requests

api_key = "<INSERT-YOUR-API-KEY>"
network_id = "<INSERT-NETWORK-ID>"
url = "https://api.meraki.com/api/v1/networks/" + network_id + "/appliance/vlans"

payload = '''{
    "id": "2",
    "name": "VLAN_PYTHON",
    "subnet": "192.168.2.0/24",
    "applianceIp": "192.168.2.1"
}'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))