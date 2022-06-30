from flask.views import MethodView
from flask import Flask, render_template, request

import calorie
import temperature

app = Flask(__name__)


class HomePage(MethodView):
	def get(self):
		return render_template('index.html')


class CaloriesFormPage(MethodView):
	def get(self):
		calories_form = calorie.CaloriesForm()
		return render_template('calories_form_page.html', caloriesform=calories_form)

	def post(self):
		calories_form = calorie.CaloriesForm(request.form)

		# Create instances
		temp = temperature.Temperature(calories_form.country.data, calories_form.city.data).get()
		print(temp)
		calories = calorie.Calorie(int(calories_form.weight.data), int(calories_form.height.data), int(calories_form.age.data), float(temp)).calculate()

		return render_template('calories_form_page.html',
			result=True,
			caloriesform=calories_form,
			calories=calories)


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)