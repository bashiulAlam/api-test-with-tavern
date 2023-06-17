import redis

from tavern.core import run

def clear_redis_cache():
    r = redis.Redis()
    r.flushdb()
def run_tests():
    print("\n\nExecuting API tests...\n\n")
    run("test_weather-api.tavern.yaml", tavern_global_cfg={})

def run_empty_redis_validation_tests():
    print("\n\nExecuting empty redis validation tests...\n\n")
    run("test_empty-redis-cache-validation.tavern.yaml", tavern_global_cfg={})

if __name__ == "__main__":
    run_tests()
    clear_redis_cache()
    run_empty_redis_validation_tests()