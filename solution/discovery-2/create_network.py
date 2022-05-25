import requests

url = "https://api.meraki.com/api/v1/organizations/<INSERT YOUR ORG ID HERE>/networks"
api_key = "<INSERT-API-KEY-HERE>"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}

payload = {
    "name": "Meraki_Network_Demo",
    "timeZone": "America/Los_Angeles",
    "productTypes": [
        "appliance",
        "switch"
    ]
}

response = requests.request('POST', url, headers=headers, json = payload)

print(response.text.encode('utf8'))