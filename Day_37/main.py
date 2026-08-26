import requests
from datetime import datetime
USERNAME="jadjare"
TOKEN="wewls32diieswild"
GRAPH_ID="graph1"
pixela_endpoint_api="https://pixe.la/v1/users"
today=datetime.today()
user_parameter={
    "token":"wewls32diieswild",
    "username":"jadjare",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
graph_endpoint_api=f"{pixela_endpoint_api}/{USERNAME}/graphs"

graph_parameter={
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_api=f"{pixela_endpoint_api}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_parameter={
 "date":today.strftime("%Y%m%d"),
 "quantity":"8.29"
}
pixel_header={
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=pixel_api, headers=headers, json=pixel_parameter)
