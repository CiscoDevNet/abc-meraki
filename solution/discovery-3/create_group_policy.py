import requests

api_key = "<INSERT-YOUR-API-KEY>"
network_id = "<INSERT -NETWORK-ID>"
url = f"https://api.meraki.com/api/v1/networks/{network_id}/groupPolicies"

group_policy_config = open("group_policy_config.json", "r").read()

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}

response = requests.request("POST", url, headers=headers, data = group_policy_config)

print(response.text.encode("utf8"))