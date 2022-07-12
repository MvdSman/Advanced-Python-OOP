import databases as db


class Cards:
	"""
	Represents banking cards.
	"""

	def __init__(self, database):
		self.database = database

	def verify(self, card_type, card_number, cvc, holder_name, price):
		pass

	def transfer(self, card_type, card_number, cvc, holder_name):
		pass
