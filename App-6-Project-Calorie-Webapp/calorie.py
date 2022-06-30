from wtforms import Form, StringField, SubmitField


class CaloriesForm(Form):
	weight = StringField('Weight (kg): ', default='77')
	height = StringField('Height (cm): ', default='185')
	age = StringField('Age: ', default='26')

	country = StringField('Country: ', default='Netherlands')
	city = StringField('City: ', default='Amsterdam')

	button = SubmitField('Calculate')


class Calorie:
	"""
	Represents the amount of calories required today.

	Calculated by:
	BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
	"""

	def __init__(self, weight, height, age, temperature):
		self.weight = weight
		self.height = height
		self.age = age
		self.temperature = temperature

	def calculate(self):
		return 10*self.weight + 6.25*self.height - 5*self.age + 5 - 10*self.temperature


if __name__ == "__main__":
	import temperature
	temp = temperature.Temperature(country='netherlands', city='amsterdam').get()
	cal = Calorie(weight=77, height=185, age=26, temperature=temp).calculate()
	print(cal)
