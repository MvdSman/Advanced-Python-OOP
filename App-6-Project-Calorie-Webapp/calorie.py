from wtforms import Form, StringField, SubmitField


class CalorieForm(Form):
	weight = StringField('Weight (kg): ', default='77')
	height = StringField('Height (cm): ', default='185')
	age = StringField('Age: ', default='26')

	country = StringField('Country: ', default='The Netherlands')
	city = StringField('City: ', default='Amsterdam')

	button = SubmitField('Calculate')


class Calorie:
	"""
	Represents the amount of calories required today.

	Calculated by:
	BMR = 10*weight + 6.25*height - 5*age + 5 -10*temperature
	"""

	def __init__(self, weight, height, age, temperature):
		self.weight = weight
		self.height = height
		self.age = age
		self.temperature = temperature

	def calculate(self):
		pass
