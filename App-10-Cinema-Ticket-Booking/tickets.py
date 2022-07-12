import random
import string
import webbrowser
from fpdf import FPDF

import databases as db
import cards
import seats


class Account:

	def __init__(self, name):
		self.name = name

	def pay(self, card, seat):
		pass


class Transaction:
	"""
	Represents cinema seat ticket transactions.
	"""

	def __init__(self, card, seat):
		self.card = card
		self.seat = seat

	def _check_balance(self):
		if self.card.get_balance() >= self.seat.get_price():
			return True

		return False

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
		filename = f"ticket_{ticket_nr}.pdf"
		pdf.output(filename)
		webbrowser.open(filename)


	def generate_ticket(self, name):
		if self._check_balance():
			ticket_nr = self._get_string()
			print(
				f"\n====\nTICKET:\n"
				f"\rTicket nr.: {ticket_nr}\n"
				f"\rSeat nr.: {self.seat.seat_id}\n"
				f"\rFull name: {name}\n"
				f"\rCard holder: {self.card.holder_name}\n"
				f"===="
			)
			self._generate_pdf(ticket_nr, name)


			return ticket_nr
