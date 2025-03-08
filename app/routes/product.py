from fastapi import APIRouter, HTTPException
from database import DB, STAGE
from models.product import Product

router = APIRouter()

COLL = "products"

@router.post("/")
async def create_product(product: Product):
    product_dict = product.model_dump()
    result = DB[COLL].insert_one(product_dict)
    return {"id": str(result.inserted_id)}
