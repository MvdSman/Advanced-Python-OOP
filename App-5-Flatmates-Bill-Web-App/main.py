"""
To-Do list:
TODO: Expand CSS
"""
import os

from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField

from flatmates_bill import flat, reports

app = Flask(__name__)


class HomePage(MethodView):
	def get(self):
		return render_template('index.html')


class BillFormPage(MethodView):
	def get(self):
		bill_form = BillForm()
		return render_template('bill_form_page.html', billform=bill_form)

	def post(self):
		bill_form = BillForm(request.form)

		# Create instances
		the_bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
		flatmate1 = flat.Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
		flatmate2 = flat.Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))

		# Generate report
		filename = f"{the_bill.period}.pdf"
		pdf_report = reports.PdfReport(filename)
		pdf_report.generate(flatmate1, flatmate2, bill=the_bill)

		# Upload report and get link
		filesharer = reports.FileSharer(filename, api_key="your-api-key")  # TODO: Add API key yourself
		url = filesharer.share()

		return render_template('bill_form_page.html',
			result=True,
			billform=bill_form,
			name1=flatmate1.name, amount1=flatmate1.pays(the_bill, flatmate2),
			name2=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1),
			url=url)


class ResultsPage(MethodView):
	def post(self):
		bill_form = BillForm(request.form)

		the_bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
		flatmate1 = flat.Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
		flatmate2 = flat.Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))

		return render_template('results.html',
			name1=flatmate1.name, amount1=flatmate1.pays(the_bill, flatmate2),
			name2=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
	amount = StringField('Bill Amount: ', default='160')
	period = StringField('Bill Period: ', default='June 2022')

	name1 = StringField('Name: ', default='John')
	days_in_house1 = StringField('Days in the house: ', default='20')

	name2 = StringField('Name: ', default='Mary')
	days_in_house2 = StringField('Days in the house: ', default='28')

	button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)  # TODO: Remove if you want to run this as a Flask app on www.pythonanywhere.com
