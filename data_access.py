import sqlite3
from helpers import dict_factory
from app_config import AppConfig

config = AppConfig()
db_path = config.get_db_path()

#Access Layout
def add_layout(id, name):
    sql = """
		INSERT INTO layout (layout_id, name) 
		VALUES (:id, :name)
		ON CONFLICT(layout_id) DO UPDATE SET name= :name;
		"""
    try:
        with sqlite3.connect(db_path) as connection:
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
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = dict_factory
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
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = dict_factory
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
        with sqlite3.connect(db_path) as connection:
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
        with sqlite3.connect(db_path) as connection:
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
        with sqlite3.connect(db_path) as connection:
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
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute(sql, {"id": id})
        all_decoders = cursor.fetchall()
        return all_decoders

def get_single_decoder(id, nr):
    sql = """
		SELECT *
        FROM decoder
        WHERE layout_id = :id AND decoder_nr = :nr;
		"""
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = dict_factory
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
        with sqlite3.connect(db_path) as connection:
            connection.execute(sql, {"id": id, "nr": nr})
            result = {'status': 1, 'message': 'Decoder Edited'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result


def delete_decoder(id, nr):
    sql = """
		DELETE FROM decoder
        WHERE layout_id = :id AND decoder_nr = :nr;
		"""
    try:
        with sqlite3.connect(db_path) as connection:
            connection.execute(sql, {"id": id, "nr": nr})
            result = {'status': 1, 'message': 'Decoder Deleted'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result

    #Access Screen

def add_screen(id, nr, fullscreen):
    sql = """
		INSERT INTO screen (layout_id,screen_nr, fullscreen) 
		VALUES (:id, :nr, :fullscreen)
		ON CONFLICT(layout_id, screen_nr) DO UPDATE SET fullscreen = :fullscreen;
		"""
    try:
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, {"id": id, "nr": nr, "fullscreen": fullscreen})
            result = {'status': 1, 'message': 'Screen Added'}
    except:
        result = {'status': 0, 'message': 'error'}
    return result


def get_all_screens(id):
    sql = """
        SELECT * FROM screen
        WHERE layout_id = :id;
        """
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute(sql, {"id": id})
        all_screens = cursor.fetchall()
        return all_screens

def get_single_screen(id, nr):
    sql = """
		SELECT *
        FROM screen
        WHERE layout_id = :id AND screen_nr = :nr;
		"""
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute(sql, {"id": id, "nr": nr})
        screen = cursor.fetchone()
        return screen


def edit_sreen_value(id, nr, value):
    sql = """
		UPDATE screen
        SET fullscreen = :fullscreen
        WHERE layout_id = :id AND screen_nr = :nr ;
		"""
    try:
        with sqlite3.connect(db_path) as connection:
            connection.execute(sql, {"id": id, "nr": nr})
            result = {'status': 1, 'message': 'Screen Edited'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result


def delete_screen(id, nr):
    sql = """
		DELETE FROM screen
        WHERE layout_id = :id AND screen_nr = :nr;
		"""
    try:
        with sqlite3.connect(db_path) as connection:
            connection.execute(sql, {"id": id, "nr": nr})
            result = {'status': 1, 'message': 'Screen Deleted'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result
