import json

class JsonReader:
    @staticmethod
    def read_json(file_path):
        """Deserializes any given JSON file path into a Python dict."""
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)