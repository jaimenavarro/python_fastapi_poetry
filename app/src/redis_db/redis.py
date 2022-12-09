import redis
import json

from app.src.config import config

db_redis = redis.Redis(host=f'{config.REDIS_DB_SERVER}', port=config.REDIS_DB_PORT, db=config.REDIS_DB_NUMBER)


def get_redis_value(key):
    return json.loads(db_redis.get(key))


def set_redis_value(key, value):
    return db_redis.set(key, value.json())
