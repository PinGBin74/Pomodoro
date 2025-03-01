import redis

from database.database import settings
from settings import Settings


def get_redis_connection() -> redis.Redis:
    return redis.Redis(
        host=settings.CACHE_HOST, port=settings.CACHE_PORT, db=settings.CACHE_DB
    )
