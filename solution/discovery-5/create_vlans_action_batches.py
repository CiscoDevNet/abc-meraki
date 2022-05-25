import requests

API_KEY = "<INSERT-YOUR-API-KEY>"
organization_id = "<INSERT-ORGANIZATION-ID>"
network_id = "<INSERT-NETWORK-ID>"
tags = ["action_batches"]

url = f"https://api.meraki.com/api/v1/organizations/{organization_id}/actionBatches"

payload = {
    "confirmed": True,
    "synchronous": True,
    "actions": [
        {
            "resource": f"/networks/{network_id}/vlans",
            "operation": "create",
            "body": {
                "id": 3,
                "name": " VLAN_ACTION_BATCHES_1",
                "applianceIp": "192.168.3.1",
                "subnet": "192.168.3.0/24",
            },
        },
        {
            "resource": f"/networks/{network_id}/vlans",
            "operation": "create",
            "body": {
                "id": 4,
                "name": " VLAN_ACTION_BATCHES_2",
                "applianceIp": "192.168.4.1",
                "subnet": "192.168.4.0/24",
            },
        },
    ],
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)