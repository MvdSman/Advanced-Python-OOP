import requests
from selectorlib import Extractor


class Temperature:
	"""
	Represents the temperature value extracted from the webpage www.timeanddate.com/weather.
	"""

	def __init__(self, country, city):
		self.country = country
		self.city = city

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

	def get(self, extractor_file='temperature.yaml'):
		# Download page
		url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
		req = requests.get(url=url, headers=self.headers)

		# Extract element(s): return False on invalid response
		content = False
		if str(req) == '<Response [200]>':
			extractor = Extractor.from_yaml_file(extractor_file)
			content = extractor.extract(req.text)
			content = float(content['temp'].replace('\xa0°C', '').strip())
		else:
			print(f'URL response: {req}')

		return content


# temp = Temperature(country='netherlands', city='amsterdam')
# temp_content = temp.get()
# print(temp_content)
