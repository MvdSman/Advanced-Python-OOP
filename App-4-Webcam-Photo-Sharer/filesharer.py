from filestack import Client

class FileSharer:
	"""
	Object that interfaces with an API to share files.

	IMPORTANT: relies on a FileStack API key!
	"""
	def __init__(self, filepath, api_key):
		self.filepath = filepath
		self.api_key = api_key

	def share(self):
		client = Client(self.api_key)
		filelink = client.upload(filepath=self.filepath)
		return filelink.url