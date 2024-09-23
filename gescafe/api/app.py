from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from pymongo import MongoClient
import db

APP_NAME = "GesCafe"
AUTHORS = ["Pedro Villarroel"]
VERSION = "0.0.1"
CLIENT = MongoClient("mongodb://localhost:27017")

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float

class ItemSold(BaseModel):
    item_id: str
    quantity: int
    seller: str = None
    ticket_id: str = None
    
@app.get("/")
def read_root():
    return {"app": APP_NAME,
            "authors":AUTHORS,
            "version":VERSION}


@app.post("/sell")
def sell_item(transaction:ItemSold):
    product = db.get_product(transaction.item_id, CLIENT)
    message =f"Sold {transaction.quantity} of {product['name']}"
    if transaction.seller:
        message += f" by {transaction.seller}"
    total = product['price']*transaction.quantity
    if not ticket_id:
        ticket_id = db.create_ticket(seller)
    
    return {"message": message,
            "total":total}

@app.put("/create")
def create_item(item: Item):
    print(CLIENT["CAFE"]["Products"].update_one({"name":item.name},
                                          {"$set": {"name":item.name,
                                                    "price":item.price}},upsert=True))
    message =f"Created {item.name} of price: {item.price} ARS"
    return {"message": message}

