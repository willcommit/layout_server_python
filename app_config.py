import json
from enum import Enum

class Settings (Enum):
    port = 1
    db_path = 2
    layout_amount = 3

def read_setting(setting):
    with open('settings.json', 'r') as json_file:
        settings = json.load(json_file)
        if setting == Settings.port:
            return settings['port']
        elif setting == Settings.db_path:
            return settings['database']['path']
        elif setting == Settings.layout_amount:
            return settings['layout_amount']

def write_setting(setting, value):

    with open('settings.json', 'r') as json_file:
        settings = json.load(json_file)
        if setting == Settings.port:
            settings['port'] = value
        elif setting == Settings.db_path:
            settings['database']['path'] = value
        elif setting == Settings.layout_amount:
            settings['layout_amount'] = value

    with open("settings.json", "w") as json_file:
        json.dump(settings, json_file, indent=4)
