import requests
from pprint import pprint

url = "https://api.meraki.com/api/v1/organizations/"
api_key = "<INSERT API KEY HERE>"
payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}

response = requests.request('GET', url, headers=headers, data = payload)

pprint(response.json())