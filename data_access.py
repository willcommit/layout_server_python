import json
import sqlite3
from app_config import *

#Access Layout

def add_layout(id, name):
    sql = """
		INSERT INTO layout (layout_id, name) 
		VALUES (:id, :name)
		ON CONFLICT(layout_id) DO UPDATE SET name= :name;
		"""
    try:
        with sqlite3.connect(read_setting(Settings.db_path)) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, {"id": id, "name": name})
            result = {'status': 1, 'message': 'Layout Added'}
    except:
        result = {'status': 0, 'message': 'error'}
    return result


def get_all_layouts():
    sql = """
        SELECT * FROM layout;
        """
    with sqlite3.connect(read_setting(Settings.db_path)) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        all_songs = cursor.fetchall()
        return all_songs


def get_single_layout(layout_id):
    sql = """
		SELECT *
        FROM layout
        WHERE layout_id = :id;
		"""
    with sqlite3.connect(read_setting(Settings.db_path)) as connection:
        cursor = connection.cursor()
        cursor.execute(sql, {"id": layout_id})
        layout = cursor.fetchone()
        return layout


def edit_layout_name(id, name):
    sql = """
		UPDATE layout
        SET name = :name
        WHERE layout_id = :id;
		"""
    try:
        with sqlite3.connect(read_setting(Settings.db_path)) as connection:
            connection.execute(sql, {"id": id, "name": name})
            result = {'status': 1, 'message': 'Layout Edited'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result


def delete_layout(layout_id):
    sql = """
		DELETE FROM layout
        WHERE layout_id = :id;
		"""
    try:
        with sqlite3.connect(read_setting(Settings.db_path)) as connection:
            connection.execute(sql, {"id": layout_id})
            result = {'status': 1, 'message': 'Layout Deleted'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result



#Access Decoder 