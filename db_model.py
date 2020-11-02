import sqlite3
from app_config import AppConfig

config = AppConfig()

CREATE_LAYOUT = """CREATE TABLE layout (
	layout_id INTEGER PRIMARY KEY NOT NULL CHECK(layout_id >= 1 AND layout_id <= 16) UNIQUE,
	name TEXT
	);
	"""

CREATE_DECODER = """CREATE TABLE decoder (
	decoder_nr INTEGER NOT NULL,
	value INTEGER NOT NULL,
	layout_id INTEGER NOT NULL, 
	PRIMARY KEY(decoder_nr,layout_id),
	FOREIGN KEY(layout_id) REFERENCES layout(layout_id) ON UPDATE SET NULL ON DELETE SET NULL
	);
	"""

CREATE_SCREEN = """CREATE TABLE screen (
	screen_nr INTEGER NOT NULL CHECK(screen_nr>=1 AND screen_nr<=6),
	fullscreen	NUMERIC NOT NULL DEFAULT 0 CHECK(fullscreen=1 or fullscreen=0),
	layout_id INTEGER NOT NULL,
	PRIMARY KEY(screen_nr,layout_id),
	FOREIGN KEY(layout_id) REFERENCES layout(layout_id) ON UPDATE SET NULL ON DELETE SET NULL
	);
	"""

def create_db():
	with sqlite3.connect(config.get_db_path()) as connection:
		c = connection.cursor() 
		c.execute(CREATE_LAYOUT)
		c.execute(CREATE_DECODER)
		c.execute(CREATE_SCREEN)
		print("DB created successfully")
	return True

def populate_layout_data():

	sql = """
		INSERT INTO layout (layout_id, name) 
		VALUES (:id, :name)
		ON CONFLICT(layout_id) DO UPDATE SET name= :name
		"""

	with sqlite3.connect(config.get_db_path()) as connection:
		cursor = connection.cursor()
		for i in range(16):
			i += 1
			cursor.execute(sql, {"id": i, "name": "Layout {}".format(i)})
	print("Layout data populated")

if __name__ == '__main__':
	create_db()
	populate_layout_data()