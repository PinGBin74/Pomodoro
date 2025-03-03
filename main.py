from fastapi import FastAPI, APIRouter
from handlers import routers


app = FastAPI()

for router in routers:
    app.include_router(router)
