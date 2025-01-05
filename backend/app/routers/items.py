from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
async def read_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]
