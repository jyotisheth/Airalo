import os
import json

class Config:
    def __init__(self):
        self.config = json.loads(open("../config.json").read())

    def base_url(self):
        return self.config["default"]["API_BASE_URL"]