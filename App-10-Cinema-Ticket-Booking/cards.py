import databases as db


class Cards:
	"""
	Represents banking cards.
	"""

	def __init__(self, database, card_type, card_number, cvc, holder_name):
		self.table_name = "Card"
		self.database = database
		self.card_type = card_type
		self.card_number = card_number
		self.cvc = cvc
		self.holder_name = holder_name

	def verify(self):
		result = db.select_records(self.table_name, self.database, '*',
		                           f'"type"=="{self.card_type}" AND '
		                           f'"number"=="{self.card_number}" AND '
		                           f'"cvc"=="{self.cvc}" AND '
		                           f'"holder"=="{self.holder_name}"')
		print(result)
		print(len(result))

		if len(result) == 1:
			return True

		return False

	def get_balance(self):
		result = db.select_records(self.table_name, self.database, '"balance"',
		                           f'"type"=="{self.card_type}" AND '
		                           f'"number"=="{self.card_number}" AND '
		                           f'"cvc"=="{self.cvc}" AND '
		                           f'"holder"=="{self.holder_name}"')
		if result:
			balance = float(result[0][0])
			print(balance)
			return balance

	def transfer(self, value):
		old_balance = self.get_balance()
		db.update_records(self.table_name, self.database, f'"balance"={old_balance - value}',
						  f'"type"=="{self.card_type}" AND '
						  f'"number"=="{self.card_number}" AND '
						  f'"cvc"=="{self.cvc}" AND '
						  f'"holder"=="{self.holder_name}"')
		new_balance = self.get_balance()
		print(f"Transfer done: {old_balance} -> {new_balance}")
		return float(new_balance)
