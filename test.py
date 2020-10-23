import json
import configparser

config = configparser.ConfigParser()
config.read('settings.json')
config.sections()