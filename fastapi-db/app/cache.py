import redis
import os
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True
)

def set_cache(key, value):
    r.set(key, value)

def get_cache(key):
    return r.get(key)
