DB_NAME = "adease"
MONGODB_URL = "mongodb://localhost:27017/"

# mongodb connection string
MONGODB_CON_STR = "{}{}".format(MONGODB_URL, DB_NAME)

# Redis cache
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = MONGODB_CON_STR
CACHE_TYPE = "redis"
CACHE_REDIS_HOST = "redis"
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = 0
CACHE_REDIS_URL = "redis://localhost:6379/0"
CACHE_DEFAULT_TIMEOUT = 500