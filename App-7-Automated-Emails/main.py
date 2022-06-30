import requests
from datetime import date, timedelta

class NewsFeed:
	"""
	Object that gets news articles from the https://newsapi.org/v2/ API.

	Requires an API key!
	"""
	def __init__(self, from_date, to_date, language='en', api_key='YOUR-API-KEY'):
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

	def get(self, interest):
		"""
		Gets the news articles of the last day based on an interest in the title.

		:return: dictionary of articles.
		"""
		url = self._build_url(interest)
		req = requests.get(url)
		return req.json()['articles']


if __name__ == "__main__":
	articles = NewsFeed(
		from_date=date.today() - timedelta(days=1),
		to_date=date.today(),
		language='en'
	).get('The Netherlands')

	email_body = ''
	for article in articles:
		email_body = email_body + article['title'] + ':\n' +\
		             '\t' + article['author'] + '\n' +\
		             '\t' + article['url'] + '\n\n'

	print(email_body)
