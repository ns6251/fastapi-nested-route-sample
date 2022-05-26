from fastapi import APIRouter

router = APIRouter(prefix="/items")


@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello world by items"}
