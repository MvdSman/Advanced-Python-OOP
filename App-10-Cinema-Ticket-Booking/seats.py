import databases as db


class Seats:
	"""
	Represents cinema seats.
	"""

	def __init__(self, database):
		self.database = database

	def is_free(self, seat_id):
		pass

	def claim(self, seat_id):
		pass
