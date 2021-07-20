# Day 37: Habit Tracking Project - API Post Requests & Headers
import datetime
import requests

# Creating a new pixela account
USERNAME = "diego95"
TOKEN = "dfsjkslfj234ijkfijg"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a new graph inside pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Driving Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Creating a new pixel within the existing graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
todays_date = str(datetime.datetime.now().date()).replace("-", "")
today = datetime.datetime(2021, 7, 19)
# today = datetime.datetime.now()
today = today.strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "5",
}

# response = requests.post(
#     url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# Updating an existing pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
pixel_update_config = {
    "quantity": "2.5"
}

# response = requests.put(url=pixel_update_endpoint,
#                         json=pixel_update_config, headers=headers)
# print(response.text)


# Deleteing an existing pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
