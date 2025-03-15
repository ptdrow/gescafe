import requests

base_url = "http://127.0.0.1:8000"
response = requests.get(base_url)
print(response.json())

endpoint = "/api/token"
response = requests.post(base_url + endpoint, data={"username":"tester",
                                                    "password":"1234"})
token = response.json()["access_token"]
#Create products
endpoint = "/api/products/"
response = requests.post(base_url+endpoint,
                         json={"name": "Café grande",
                               "price": 3800,
                               "stock": 0},
                         headers={"Authorization": f"Bearer {token}"})


