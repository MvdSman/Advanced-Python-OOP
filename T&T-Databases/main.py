import sqlite3


def create_table():
	"""
	Create the Seat table.

	:return:
	"""
	connection = sqlite3.connect("cinema.db")
	connection.execute(
		"""
		CREATE TABLE "Seat" (
			"seat_id"	TEXT,
			"taken"	INTEGER,
			"price"	REAL,
			PRIMARY KEY("seat_id")
		);
		"""
	)
	connection.commit()
	connection.close()


def insert_record(record, table_name, database):
	"""
	Insert a record into a table.

	:param record: record values to insert.
	:param table_name: name of the table.
	:param database: database to connect to.

	:return:
	"""
	connection = sqlite3.connect(database)
	connection.execute(
		f"""
		INSERT INTO {table_name} (
			"seat_id", "taken", "price"
		) VALUES {record}
		"""
	)
	connection.commit()
	connection.close()


def select_all(table_name, database):
	"""
	Selects all records from a table.

	:param table_name: name of the table.
	:param database: database to connect to.

	:return: Query result.
	"""
	connection = sqlite3.connect(database)
	cursor = connection.cursor()
	cursor.execute(
		f"""
		SELECT * FROM {table_name}
		"""
	)
	result = cursor.fetchall()
	connection.close()

	return result


def select_columns(table_name, database, columns, condition=None):
	"""
	Selects all records' columns from a table.

	:param table_name: name of the table.
	:param database: database to connect to.
	:param columns: columns to select.
	:param condition: optional condition to filter on (after the WHERE clause).

	:return: Query result.
	"""
	connection = sqlite3.connect(database)
	cursor = connection.cursor()
	if condition:
		cursor.execute(
			f"""
			SELECT {columns} FROM {table_name} WHERE {condition}
			"""
		)
	else:
		cursor.execute(
			f"""
			SELECT {columns} FROM {table_name}
			"""
		)
	result = cursor.fetchall()
	connection.close()

	return result


def update_record(table_name, database, update, condition=None):
	"""
	Updates records of a table.

	:param table_name: name of the table.
	:param database: database to connect to.
	:param update: update query (after the SET clause).
	:param condition: optional condition to filter on (after the WHERE clause).

	:return:
	"""
	connection = sqlite3.connect(database)
	if condition:
		connection.execute(
			f"""
			UPDATE {table_name} SET {update} WHERE {condition}
			"""
		)
	else:
		connection.execute(
			f"""
			UPDATE {table_name} SET {update}
			"""
		)
	connection.commit()
	connection.close()


def delete_record(table_name, database, condition=None):
	"""
	Deletes records from a table.

	:param table_name: name of the table.
	:param database: database to connect to.
	:param condition: optional condition to filter on (after the WHERE clause).

	:return:
	"""
	connection = sqlite3.connect(database)
	if condition:
		connection.execute(
			f"""
			DELETE FROM {table_name} WHERE {condition}
			"""
		)
	else:
		connection.execute(
			f"""
			DELETE FROM {table_name}
			"""
		)
	connection.commit()
	connection.close()


create_table()

values = [
	("A1", "0", "90"),
	("A2", "1", "100"),
	("A3", "0", "80")
]

for record in values:
	insert_record(record, "Seat", "cinema.db")

select_all("Seat", "cinema.db")
select_columns("Seat", "cinema.db", '"seat_id", "taken"')
select_columns("Seat", "cinema.db", '"seat_id", "taken"', '"taken" == 1')
update_record("Seat", "cinema.db", '"taken"=1', '"seat_id" == "A3"')
delete_record("Seat", "cinema.db", '"seat_id" == "A3"')
