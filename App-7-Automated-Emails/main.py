import requests
from datetime import date, timedelta

class NewsFeed:
	"""
	Object that gets news articles from the https://newsapi.org/v2/ API.

	Requires an API key!
	"""
	def __init__(self, data, api_key='YOUR-API-KEY'):
		self.data = data
		self.api_key = api_key

	def _build_url(self, interest):
		return f'https://newsapi.org/v2/everything?' \
		       f'qInTitle={interest}&' \
		       f'from={date.today() - timedelta(days=1)}&' \
		       f'to={date.today()}&' \
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
	news = NewsFeed(data='').get('The Netherlands')
	print(news[0]['title'])
