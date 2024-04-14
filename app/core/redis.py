import logging
from datetime import timedelta
from typing import Optional

import redis.asyncio as aioredis
from settings import config_parameters
from pydantic import BaseModel

logger = logging.getLogger(__name__)
pool = aioredis.ConnectionPool.from_url(
    f"redis://{config_parameters.REDIS_HOST}:{config_parameters.REDIS_PORT}/{config_parameters.REDIS_DATABASE}",
    max_connections=10, decode_responses=True,
)
redis_client = aioredis.Redis(connection_pool=pool)


class RedisData(BaseModel):
    key: bytes | str
    value: bytes | str
    ttl: Optional[int | timedelta] = None


async def __set_redis_key(
    redis_data: RedisData, *, is_transaction: bool = False
) -> None:
    async with redis_client.pipeline(transaction=is_transaction) as pipe:
        await pipe.set(redis_data.key, redis_data.value)
        if redis_data.ttl:
            await pipe.expire(redis_data.key, redis_data.ttl)

        await pipe.execute()


async def set_by_key(key: str, value: str, ttl: int | timedelta | None = None) -> None:
    return await __set_redis_key(RedisData(key=key, value=value, ttl=ttl))


async def get_by_key(key: str) -> str | None:
    return await redis_client.get(key)


