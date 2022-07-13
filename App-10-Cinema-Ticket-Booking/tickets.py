import random
import string
import webbrowser
import os
from fpdf import FPDF

import databases as db
import cards
import seats


class Account:
	"""
	Repesents a user account on the booking app.
	"""
	def __init__(self, name):
		self.name = name

	def _check_balance(self, card, seat):
		if card.get_balance() >= seat.get_price():
			return True
		else:
			return False

	def _checkout(self, card, seat):
		curr_balance = card.transfer(seat.get_price())
		return curr_balance

	def pay(self, card, seat):
		if self._check_balance(card, seat):
			self._checkout(card, seat)
			seat.claim()
			ticket_nr = Ticket(card, seat, self.name).generate_ticket()
			return ticket_nr
		else:
			return None


class Ticket:
	"""
	Represents cinema seat ticket transactions.
	"""
	def __init__(self, card, seat, name):
		self.card = card
		self.seat = seat
		self.name = name

	def _get_string(self, length=6):
		characters = string.ascii_letters + string.digits
		result_str = ''.join(random.choice(characters) for i in range(length))
		return result_str

	def _generate_pdf(self, ticket_nr, name):
		pdf = FPDF(orientation='P', unit='pt', format='A4')
		pdf.add_page()

		# Insert title
		pdf.set_font(family='Times', size=24, style='B')
		pdf.cell(w=0, h=80, txt="Ticket confirmation", border=0, align="C", ln=1)

		# Insert Ticket label and value
		pdf.set_font(family="Times", size=14, style='B')
		pdf.cell(w=100, h=40, txt="Ticket nr.:", border=0)
		pdf.cell(w=150, h=40, txt=ticket_nr, border=0, ln=1)

		# Insert seat
		pdf.set_font(family="Times", size=12)
		pdf.cell(w=100, h=25, txt="Seat nr.:", border=0)
		pdf.cell(w=150, h=25, txt=self.seat.seat_id, border=0, ln=1)

		# Insert your name
		pdf.set_font(family="Times", size=12)
		pdf.cell(w=100, h=25, txt="Full name:", border=0)
		pdf.cell(w=150, h=25, txt=name, border=0, ln=1)

		# Change directory to files, generate and open the PDF
		os.chdir("tickets")
		filename = f"ticket_{self.seat.seat_id}_{ticket_nr}.pdf"
		pdf.output(filename)
		webbrowser.open(filename)

	def generate_ticket(self):
		ticket_nr = self._get_string()
		print(
			f"\n====\nTICKET:\n"
			f"\rTicket nr.: {ticket_nr}\n"
			f"\rSeat nr.: {self.seat.seat_id}\n"
			f"\rFull name: {self.name}\n"
			f"\rCard holder: {self.card.holder_name}\n"
			f"===="
		)
		self._generate_pdf(ticket_nr, self.name)
		return ticket_nr
