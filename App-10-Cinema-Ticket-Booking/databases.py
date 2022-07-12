import sqlite3


def select_records(table_name, database, columns, condition=None):
	"""
	Gets all records' fields from a table.

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


def update_records(table_name, database, update, condition=None):
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


def delete_records(table_name, database, condition=None):
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


if __name__ == "__main__":
    select_records("Seat", "cinema.db", '"seat_id", "taken"')
    select_records("Seat", "cinema.db", '"seat_id", "taken"', '"taken" == 1')
    update_records("Seat", "cinema.db", '"taken"=1', '"seat_id" == "A3"')
    delete_records("Seat", "cinema.db", '"seat_id" == "A3"')
