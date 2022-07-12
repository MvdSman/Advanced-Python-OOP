import cards
import seats
import tickets


class CliUI:

	def __init__(self):

	def get_seat(self, seats_list):
		full_name = input("Enter your full name: ")

		free_seat = False
		while not free_seat:
			seat_id = input("Enter your preferred seat number: ")
			free_seat = seats_list.is_free(seat_id)
			if not free_seat:
				print(f"Seat {seat_id} was already taken! Please try again.")

		return full_name, seat_id


	def get_card(self, seat_price, cards_list):
		card_valid = False

		while not card_valid:
			card_type = input("Enter your card type: ")
			card_number = int(input("Enter your card number: "))
			cvc = int(input("Enter your card cvc: "))
			holder_name = input("Enter your card holder name: ")
			card_valid = cards_list.verify(card_type, card_number, cvc, holder_name, seat_price)
			if not card_valid:
				print("Your card information was invalid, please try again!")

		return card_type, card_number, cvc, holder_name


if __name__ == "__main__":
	all_seats = seats.Seats()
	all_cards = cards.Cards()

	full_name, seat_id = CliUI.get_seat(all_seats)
	card_type, card_number, cvc, holder_name = CliUI.get_card(all_cards)
