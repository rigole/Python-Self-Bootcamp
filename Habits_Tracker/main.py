import requests
from datetime import datetime

USERNAME = "placide"
TOKEN = "htos654258963hjndskclASED"
GRAPH_ID = "graph01"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)

#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"              

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "KM",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/<graphID>"

today = datetime.now()


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74",
}

#response = requests.post(url=graph_endpoint, json=graph_config) 

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

print(response)
