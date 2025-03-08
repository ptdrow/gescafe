import requests

domain = "http://127.0.0.1:8000"
#Create item
##endpoint = "/create"
##url = domain+endpoint
##response = requests.put(url,json={"name":"Café",
##                                   "price":2000.0})

# Sell item
endpoint = "/sell"
item_id = "66f0a59c4f4e6379d9c82a80"
url = domain+endpoint
response = requests.post(url,json={"item_id":item_id,
                                   "quantity":5,
                                   "seller":"Pedro"})

print(response.text)

