import requests
from selectorlib import Extractor


class Temperature:
	"""
	Represents the temperature value extracted from the webpage www.timeanddate.com/weather.
	"""

	def __init__(self, country, city):
		self.country = country.replace(' ', '-')
		self.city = city.replace(' ', '-')

		# Add headers to prevent 403 error
		self.headers = {
			'pragma': 'no-cache',
			'cache-control': 'no-cache',
			'dnt': '1',
			'upgrade-insecure-requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/102.0.1245.44',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		}

	def _set_url(self):
		"""
		Sets the URL based on inputs `country` and `city`.
		:return: Full URL to scrape.
		"""
		return f'https://www.timeanddate.com/weather/{self.country}/{self.city}'

	def _scrape(self, extractor_file):
		"""
		Scrapes web-page and extracts values as instructed by the `extractor_file`.
		:param extractor_file: YAML-file describing what to extract.
		:return: dictionary of extracted values.
		"""
		# Download page
		url = self._set_url()
		req = requests.get(url=url, headers=self.headers)

		# Extract element(s): return False on invalid response
		content = False
		if str(req) == '<Response [200]>':
			extractor = Extractor.from_yaml_file(extractor_file)
			content = extractor.extract(req.text)
		else:
			print(f'URL response: {req}')

		return content

	def get(self, extractor_file='temperature.yaml'):
		"""
		Cleans the output of `_scrape()`
		:param extractor_file: YAML-file describing what to extract.
		:return: Extracted values (cleaned).
		"""
		content = self._scrape(extractor_file)

		# Clean output
		content = float(content['temp'].replace('\xa0°C', '').strip()) if content else -999

		return content


if __name__ == "__main__":
	temp = Temperature(country='netherlands', city='amsterdam')
	temp_content = temp.get()
	print(temp_content)
