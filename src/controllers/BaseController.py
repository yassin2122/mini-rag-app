from helpers.config import settings,get_settings

class Basecontroller:
    def __init__(self, settings: settings):
        self.settings = get_settings()