import cards
import seats
import tickets


class CliUI:

	def __init__(self):
		pass

	def get_seat(self):
		full_name = input("Enter your full name: ")

		free_seat = False
		while not free_seat:
			seat_id = input("Enter your preferred seat number: ")
			seat = seats.Seats("cinema.db", seat_id)
			free_seat = seat.is_free()
			if not free_seat:
				print(f"Seat {seat_id} was already taken! Please try again.")

		return full_name, seat

	def get_card(self):
		card_valid = False

		while not card_valid:
			card_type = input("Enter your card type: ")
			card_number = int(input("Enter your card number: "))
			cvc = int(input("Enter your card cvc: "))
			holder_name = input("Enter your card holder name: ")
			card = cards.Cards("banking.db", card_type, card_number, cvc, holder_name)
			card_valid = card.verify()
			if not card_valid:
				print("Your card information was invalid, please try again!")

		return card


if __name__ == "__main__":

	# Get info
	UIHost = CliUI()
	account, seat = UIHost.get_seat()
	card = UIHost.get_card()

	# Process transaction
	transaction = tickets.Transaction(card, seat)
	ticket = transaction.generate_ticket(account)


	print("Done!")
