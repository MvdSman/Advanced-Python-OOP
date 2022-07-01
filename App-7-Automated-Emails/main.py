import requests
from datetime import date, timedelta
import pandas as pd

import emailer

class NewsFeed:
	"""
	Object that gets news articles from the https://newsapi.org/v2/ API.
	Default from the last day and english only.

	Requires an API key!
	"""
	def __init__(self,
	             from_date=date.today() - timedelta(days=1), to_date=date.today(),
	             language='en', api_key='YOUR-API-KEY'):
		self.from_date = from_date
		self.to_date = to_date
		self.language = language
		self.api_key = api_key

	def _build_url(self, interest):
		return f'https://newsapi.org/v2/everything?' \
		       f'qInTitle={interest}&' \
		       f'from={self.from_date}&' \
		       f'to={self.to_date}&' \
		       f'language={self.language}&' \
		       f'sortBy=popularity&' \
		       f'apiKey={self.api_key}'

	def _build_email(self, interest, req):
		email_body = ''
		print(interest)
		if req:
			for article in req:
				email_body = f"{email_body}{article['title']}:\n\t" \
				             f"{article['author']}\n\t" \
				             f"{article['url']}\n\n"
		else:
			email_body = f"Sadly, no news updates were found for '{interest}'!\n\n"
		return email_body

	def get(self, interest, verbose=False):
		"""
		Gets the news articles of the last day based on an interest in the title.

		:param interest: keyword that should be present in titles of the articles.
        :param verbose: boolean to enable printing the email body in the console (default False).
		:return: dictionary of articles.
		"""
		url = self._build_url(interest)
		req = requests.get(url).json()['articles']

		email_body = self._build_email(interest, req)

		if verbose:
			print(email_body)
		return email_body


def send_email(emailer_class, articles_class, subscriber):
	emailer_class.send(
		to=subscriber['email'],
		subject=f"Your {subscriber['interest']} news for today!",
		contents=f"Hi {subscriber['name']},\n\n"
		         f"See what's on about {subscriber['interest']} today.\n\n"
		         f"{articles_class.get(subscriber['interest'], verbose=False)}\n\n"
		         f"Script Mailer."
	)


if __name__ == "__main__":

	df = pd.read_excel('people.xlsx')
	emailer = emailer.Mailer()
	articles = NewsFeed(
		api_key='YOUR-API-KEY'
	)

	for index, row in df.iterrows():
		send_email(emailer, articles, row)
