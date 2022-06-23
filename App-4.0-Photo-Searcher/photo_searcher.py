from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests
import textwrap  # use to split a line on word groups

# Load the kivy config file
Builder.load_file("photo_searcher.kv")


class FirstScreen(Screen):
	"""
	The first screen of the app: one screen class per screen required.
	"""
	def get_image_page(self):
		# Get user query from TextInput
		query = self.manager.current_screen.ids.user_query.text

		# Get Wikipedia page and first of the list of image URLs
		## To prevent ambiguous search results, first see the results of a Wikipedia search
		wiki_res = wikipedia.search(query)

		## Iterate through the search results until there's a non-unambiguous page result
		i = 0
		page_empty = True
		while page_empty:
			try:
				page = wikipedia.page(wiki_res[i])
			except wikipedia.exceptions.DisambiguationError:
				page_empty = True
				i += 1
			else:
				page_empty = False
				return page

	def get_image_data(self, img_path, char_per_line=100):
		page = self.get_image_page()
		img_link = page.images[0]
		lines = textwrap.wrap(page.summary, char_per_line)
		wiki_summary = '\n'.join(lines)
		print(f"Lines to show: {len(lines)}")
		print(wiki_summary)

		# Add headers to prevent 403 error
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/102.0.1245.44"
		}

		# Download image
		req = requests.get(img_link, headers=headers)
		print(f"Image link: {req}")
		with open(img_path, "wb") as file:
			file.write(req.content)
		return wiki_summary

	def set_screen(self):
		img_path = "files/photo_searcher.jpg"
		# Instead of adding "source: 'files/sample.png'" to the Image kivy element, set source here
		# self.manager.current_screen.ids.img.source = "files/sample.png" # hard-coded
		wiki_summary = self.get_image_data(img_path)
		self.manager.current_screen.ids.img.source = img_path
		self.manager.current_screen.ids.img.reload()  # Reload image upon new request
		self.manager.current_screen.ids.wiki_summary.text = wiki_summary


class RootWidget(ScreenManager):
	"""
	This class can be kept empty unless stated otherwise.
	"""
	pass


class MainApp(App):
	"""
	The object that contains the actual application.
	"""

	def build(self):
		return RootWidget()


MainApp().run()
