from fastapi import APIRouter


router = APIRouter(
    prefix="/urls",
)


@router.post("/shorten")
async def shorten():
    return {"message": "shorten"}


@router.get("/{id}")
async def get_url(id: str):
    return {"message": f"get_url: {id}"}


@router.get("/open/{short_url}")
async def open_url(short_url: str):
    return {"message": f"open_url: {short_url}"}


@router.delete("/{id}")
async def delete_url(id: str):
    return {"message": f"delete_url: {id}"}
