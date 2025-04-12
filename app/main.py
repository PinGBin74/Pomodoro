from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.tasks.handlers import router as tasks_router
from app.users.auth.handlers import router as auth_router
from app.users.user_profile.handlers import router as user_router
from app.dependecy import get_broker_consumer
import sentry_sdk

sentry_sdk.init(
    dsn="https://04d2148ccd8c18e076eee5ec852ccdfa@o4509140831305728.ingest.de.sentry.io/4509140832550992",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize broker consumer but don't start consuming
    broker_consumer = await get_broker_consumer()
    # Temporarily disable Kafka consumer
    # await broker_consumer.consume_callback_message()
    yield
    await broker_consumer.close()


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)
app.include_router(auth_router)
app.include_router(user_router)


@app.get("/app/ping")
async def ping_app():
    return {"text": "app is working"}


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0
    return {"error": "Division by zero"}
