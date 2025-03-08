from bson import ObjectId
from datetime import datetime

def get_product(item_id, client):
    doc = client["CAFE"]["Products"].find_one({"_id":ObjectId(item_id)},{"_id":0})
    return doc

def create_ticket(seller=None):
    created=datetime.now()
    result = client["CAFE"]["Tickets"].insert_one(
        {"seller":seller,
         "items": [],
         "total": 0,
         "closed":False,
         "created":created,
         "updated":created,
         }
        )
    return result.inserted_id

def update_ticket(ticket_id, added_total, name, quantity):
    client["CAFE"]["Tickets"].update_one({"_id":ObjectId(ticket_id)},
                                          {"$push":{"items":{"name":name,
                                                             "quantity":quantity,
                                                             "total":added_total}},
                                           "$inc": {"total":added_total},
                                           "$set": {"updated":datetime.now()}
                                           })
    

if __name__=="__main__":
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017")
    #print("Price:", get_product("66f0a59c4f4e6379d9c82a80",client)["price"])

    #ticket_id = create_ticket("Pedro")
    ticket_id = "66f0b3a22f26f72f8c8a3eb1"
    update_ticket(ticket_id, 1200, "Medialunas", 2)
    client.close()
