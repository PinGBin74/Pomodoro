from fastapi import FastAPI, APIRouter
from settings import Settings

router = APIRouter(prefix="/ping", tags=["ping"])


@router.get("/db")
async def ping_db():
    settings = Settings()
    return {"Message": settings.GOOGLE_TOKEN_ID}
