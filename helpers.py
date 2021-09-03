import logging
from p.schedulers.background import BackgroundScheduler
from shutil import copyfile
from datetime import datetime
import atexit
from os import mkdir, path
from app_config import AppConfig

# Proceed with starting the actual application

config = AppConfig()

def backup_job():
    backup_folder = config.get_backup_folder()
    backup_filename = config.get_backup_filename().format(timestamp = datetime.now().strftime("%y%m%d%H%M"))
    
    if not path.exists(backup_folder):
        mkdir(backup_folder)
    
    backup_path = path.join(backup_folder + backup_filename)

    try:
        copyfile(config.get_db_path(), backup_path)
    except OSError as error:
        print(error)
    
def start_backup():
    backup_time = config.get_backup_time()
    scheduler = BackgroundScheduler()  
    scheduler.add_job(backup_job, 'interval', minutes=backup_time)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
