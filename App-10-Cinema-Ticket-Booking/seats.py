import databases as db


class Seats:
	"""
	Represents cinema seats.
	"""

	def __init__(self, database, seat_id):
		self.table_name = "Seat"
		self.database = database
		self.seat_id = seat_id

	def is_free(self):
		result = db.select_records(self.table_name, self.database, '"taken"', f'"seat_id"=="{self.seat_id}"')[0][0]
		print(result)
		return not bool(int(result))

	def get_price(self):
		result = db.select_records(self.table_name, self.database, '"price"', f'"seat_id"=="{self.seat_id}"')[0][0]
		print(result)
		return float(result)

	def claim(self):
		pass
