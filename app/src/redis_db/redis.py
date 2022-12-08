import redis
import json

db_redis = redis.Redis(host='0.0.0.0', port=6379, db=0)


def get_redis_value(key):
    return json.loads(db_redis.get(key))


def set_redis_value(key, value):
    return db_redis.set(key, value.json())
