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

	def get(self, interest, verbose=False):
		"""
		Gets the news articles of the last day based on an interest in the title.

		:return: dictionary of articles.
		"""
		url = self._build_url(interest)
		req = requests.get(url).json()['articles']

		email_body = ''
		print(interest)
		if req:
			for article in req:
				email_body = f"{email_body}{article['title']}:\n\t" \
				             f"{article['author']}\n\t" \
				             f"{article['url']}\n\n"
		else:
			email_body = f"Sadly, no news updates were found for '{interest}'!\n\n"

		if verbose:
			print(email_body)
		return email_body


if __name__ == "__main__":

	df = pd.read_excel('people.xlsx')
	emailer = emailer.Mailer()
	articles = NewsFeed(
		api_key='YOUR-API-KEY'
	)

	for index, row in df.iterrows():
		emailer.send(
			to=row['email'],
			subject=f"Your {row['interest']} news for today!",
			contents=f"Hi {row['name']},\n\n"
			         f"See what's on about {row['interest']} today.\n\n"
			         f"{articles.get(row['interest'], verbose=False)}\n\n"
			         f"Script Mailer."
		)
