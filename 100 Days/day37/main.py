import requests
from datetime import datetime
USERNAME = "rebj"
TOKEN = "lkdksjfldfj"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "lkdksjfldfj",
    "username": "rebj",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph2",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
