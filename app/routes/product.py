from fastapi import APIRouter, HTTPException
from database import DB, STAGE, build_coll
from models.product import Product

router = APIRouter()

COLL = build_coll("products", STAGE)

@router.post("/")
async def create_product(product: Product):
    product_dict = product.model_dump()
    result = DB[COLL].insert_one(product_dict)
    return {"id": str(result.inserted_id)}
