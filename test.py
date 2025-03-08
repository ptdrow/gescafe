import requests

base_url = "http://127.0.0.1:8000"
response = requests.get(base_url)
print(response.json())

#Create products
endpoint = "/api/products/"
response = requests.post(base_url+endpoint, json={"name": "Café",
                                                  "price": 3500,
                                                  "stock": 0})
print(response.json())