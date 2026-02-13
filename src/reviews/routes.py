from fastapi import APIRouter

reviews_router = APIRouter(tags=["Reviews"], prefix="/reviews")
@reviews_router.get("")
async def get_reviews():
    return {"message": "List of reviews"}