from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ["MONGO_URI"]
STAGE = os.environ["STAGE"]
COFFEE_SHOP = os.environ["COFFEE_SHOP"]

client = MongoClient(MONGO_URI)
DB = client[COFFEE_SHOP]

def build_coll(coll_name, stage):
    if stage == "dev":
        return f"{stage}_{coll_name}"
    return coll_name

