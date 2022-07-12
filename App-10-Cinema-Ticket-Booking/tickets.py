import databases as db


class Ticket:
	"""
	Represents cinema seat tickets.
	"""

	def __init__(self, user, seat):
		self.user = user
		self.seat = seat

	def generate_ticket(self):
		pass
