import json
from enum import Enum

class Settings (Enum):
    port = 1
    debug = 2
    db_path = 3
    layout_amount = 4

#TODO add JSON validation
class AppConfig:

    def __init__(self):
        with open('app_config.json', 'r') as json_file:
            config = json.load(json_file)
            self.__port = config['port']
            self.__debug = config['debug']
            self.__db_path = config['database']['path']
            self.__backup_folder = config['database']['backup_folder']
            self.__backup_filename = config['database']['backup_filename']
            self.__backup_time = config['database']['backup_time_minutes']
            self.__layout_amount = config['layout_amount']

    def get_port(self):
        return self.__port

    def set_port(self, port_number):
        self.__port = port_number
        self.__write_config(Settings.port, port_number)

    def get_debug(self):
        return self.__debug
    
    def set_debug(self, debug_state):
        self.__debug = debug_state
        self.__write_config(Settings.debug, debug_state)

    def get_db_path(self):
        return self.__db_path
    
    def set_db_path(self, db_path):
        self.__db_path = db_path
        self.__write_config(Settings.db_path, db_path)

    def get_backup_folder(self):
        return self.__backup_folder
    
    def get_backup_filename(self):
        return self.__backup_filename

    def get_backup_time(self):
        return self.__backup_time

    def get_layout_amount(self):
        return self.__layout_amount

    def get_layout_amount_update(self):
        with open('app_config.json', 'r') as json_file:
            config = json.load(json_file)
            self.__layout_amount = config['layout_amount']
            return self.__layout_amount

    def set_layout_amount(self, layout_amount):
        self.__layout_amount = layout_amount
        self.__write_config(Settings.layout_amount, layout_amount)
        
    def __write_config(self, setting, value):
        with open('app_config.json', 'r') as json_file:
            settings = json.load(json_file)
            if setting == Settings.port:
                settings['port'] = value
            elif setting == Settings.db_path:
                settings['database']['path'] = value
            elif setting == Settings.layout_amount:
                settings['layout_amount'] = value
            else:
                raise KeyError('No such setting')

        with open("app_config.json", "w") as json_file:
            json.dump(settings, json_file, indent=4)      

