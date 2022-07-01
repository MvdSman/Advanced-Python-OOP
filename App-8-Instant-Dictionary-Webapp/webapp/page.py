from abc import ABC, abstractmethod

class Page(ABC):
	"""
	Abstract class to allow for automated URL routing in main.py
	"""

	@abstractmethod
	def server(self):
		pass