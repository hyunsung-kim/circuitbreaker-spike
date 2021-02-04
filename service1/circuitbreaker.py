import pybreaker
import redis

from listener import OneListener

# redis
# redis = redis.StrictRedis(host='localhost', port=6381, db=0)
# db_breaker = pybreaker.CircuitBreaker(
#     fail_max=5,
#     reset_timeout=10,
#     state_storage=pybreaker.CircuitRedisStorage(pybreaker.STATE_CLOSED, redis))

# local
db_breaker = pybreaker.CircuitBreaker(
    fail_max=5,
    reset_timeout=10,
    state_storage=pybreaker.CircuitMemoryStorage(pybreaker.STATE_CLOSED))


db_breaker.add_listeners(OneListener())


