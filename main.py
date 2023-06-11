from tavern.core import run

def run_tests():
    run("test_weather-api.tavern.yaml", tavern_global_cfg={})

if __name__ == "__main__":
    run_tests()