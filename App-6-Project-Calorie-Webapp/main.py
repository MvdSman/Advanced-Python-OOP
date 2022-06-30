from flask.views import MethodView
from flask import Flask, render_template

app = Flask(__name__)


class HomePage(MethodView):
	def get(self):
		return render_template('index.html')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

app.run(debug=True)