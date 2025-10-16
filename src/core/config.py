import yaml

LOADED = False

config = None


def load_config(path: str):
    global LOADED, config
    try:
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
            LOADED = True
            print(f"Config loaded from `{path}`")
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        raise
    except yaml.YAMLError as e:
        print(f"Error parsing config file: {e}")
        raise


def fetch_config():
    if not LOADED:
        raise RuntimeError("Config not loaded")
    return config
