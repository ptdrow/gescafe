from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ["MONGO_URI"]
STAGE = os.environ["STAGE"]
COFFEE_SHOP = os.environ["COFFEE_SHOP"]

client = MongoClient(MONGO_URI)
DB = client[COFFEE_SHOP]

