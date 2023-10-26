import json

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            with open('config.json', 'r') as config_file:
                cls._instance.data = json.load(config_file)
        return cls._instance

    @staticmethod
    def get(key):
        return Config()._instance.data.get(key)

