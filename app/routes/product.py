from fastapi import APIRouter, HTTPException, Depends
from database import DB, STAGE
from models.product import Product
from auth import get_current_user

router = APIRouter()

COLL = "products"

@router.post("/")
async def create_product(product: Product, user: str = Depends(get_current_user)):
    product_dict = product.model_dump()
    result = DB[COLL].insert_one(product_dict)
    return {"id": str(result.inserted_id)}
