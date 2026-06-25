import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def get_config():
        """Reads and caches the master config json."""
        if ConfigReader._config is None:
            # Resolves absolute path relative to utils directory
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            config_path = os.path.join(base_dir, "testdata", "master_config.json")
            with open(config_path, "r") as f:
                ConfigReader._config = json.load(f)
        return ConfigReader._config