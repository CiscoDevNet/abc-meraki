import requests

url = "https://api.meraki.com/api/v1/organizations/"
api_key = input("Please enter your API key: ")
headers = {
    "X-Cisco-Meraki-API-Key": api_key,  
    "Content-type":"application/json" 
    } 

get_all_organizations = requests.get(url, headers=headers).json()

print("This is the list of available organizations:")

for organization in get_all_organizations:
    print(f"Organization name: {organization['name']}, Organization ID: {organization['id']}") 

organization_id = input("Enter your organization ID: ")

networks = requests.get(f"{url}{organization_id}/networks", headers=headers).json()

for network in networks:
    print(f"Network name: {network['name']}, Network id: {network['id']}")