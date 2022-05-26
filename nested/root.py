from fastapi import FastAPI

from . import items, users

app = FastAPI()

app.include_router(users.router, prefix="/users") # /users
app.include_router(items.router) # /items
app.include_router(items.router, prefix="/nested") # /nested/items


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello world by root"}
