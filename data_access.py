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
        all_layouts = cursor.fetchall()
        return all_layouts


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


def delete_layout(id):
    sql = """
		DELETE FROM layout
        WHERE layout_id = :id;
		"""
    try:
        with sqlite3.connect(read_setting(Settings.db_path)) as connection:
            connection.execute(sql, {"id": id})
            result = {'status': 1, 'message': 'Layout Deleted'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result

#Access Decoder 
def add_decoder(id, nr, value):
    sql = """
		INSERT INTO decoder (layout_id,decoder_nr, value) 
		VALUES (:id, :nr, :value)
		ON CONFLICT(layout_id, decoder_nr) DO UPDATE SET value= :value;
		"""
    try:
        with sqlite3.connect(read_setting(Settings.db_path)) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, {"id": id, "nr": nr, "value": value})
            result = {'status': 1, 'message': 'Decoder Added'}
    except:
        result = {'status': 0, 'message': 'error'}
    return result


def get_all_decoders(id):
    sql = """
        SELECT * FROM decoder
        WHERE layout_id = :id;
        """
    with sqlite3.connect(read_setting(Settings.db_path)) as connection:
        cursor = connection.cursor()
        cursor.execute(sql, {"id": id})
        all_decoders = cursor.fetchall()
        return all_decoders

def get_single_decoder(nr, id):
    sql = """
		SELECT *
        FROM decoder
        WHERE layout_id = :id AND decoder_nr = :nr;
		"""
    with sqlite3.connect(read_setting(Settings.db_path)) as connection:
        cursor = connection.cursor()
        cursor.execute(sql, {"id": id, "nr": nr})
        decoder = cursor.fetchone()
        return decoder


def edit_decoder_value(id, nr, value):
    sql = """
		UPDATE decoder
        SET value = :value
        WHERE layout_id = :id AND decoder_nr = :nr ;
		"""
    try:
        with sqlite3.connect(read_setting(Settings.db_path)) as connection:
            connection.execute(sql, {"id": id, "nr": nr})
            result = {'status': 1, 'message': 'Decoder Edited'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result


def delete_decoder(id, nr):
    sql = """
		DELETE FROM layout
        WHERE layout_id = :id AND decoder_nr = :nr;
		"""
    try:
        with sqlite3.connect(read_setting(Settings.db_path)) as connection:
            connection.execute(sql, {"id": id, "nr": nr})
            result = {'status': 1, 'message': 'Decoder Deleted'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result
