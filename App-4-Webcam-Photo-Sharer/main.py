from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

from filesharer import FileSharer

# Load the kivy config file
Builder.load_file("frontend.kv")


class CameraScreen(Screen):
	"""
	The camera screen of the app: one screen class per screen required.
	"""
	def start(self):
		"""
		Starts camera and changes Button text

		:return:
		"""
		self.ids.camera.play = True
		self.ids.camera_button.text = 'Stop Camera'
		self.ids.camera.texture = self.ids.camera._camera.texture

	def stop(self):
		"""
		Stops camera and changes Button text

		:return:
		"""
		self.ids.camera.play = False
		self.ids.camera_button.text = 'Start Camera'
		self.ids.camera.texture = None

	def capture(self):
		"""
		Creates a filename with the current time and captures and saves the image under that name.

		Also initiates the switch to the Image Screen and sets the Image to the taken snapshot.

		:return:
		"""
		timestamp = time.strftime('%Y-%m-%d_%H%M%S')
		self.filepath = f"files/{timestamp}.png"
		self.ids.camera.export_to_png(self.filepath)
		self.manager.current = 'image_screen'
		self.manager.current_screen.ids.img.source = self.filepath  # Requires manager to access widget from another screen


class ImageScreen(Screen):
	"""
	The image screen of the app: one screen class per screen required.
	"""
	def create_link(self, api_key="your-api-key"):  # TODO: Add API key yourself
		"""
		Creates a link to the uploaded file on FileStack.

		Adds link to the Label widget of the ImageScreen.

		:return:
		"""
		filepath = App.get_running_app().root.ids.camera_screen.filepath
		filesharer = FileSharer(filepath, api_key)
		url = filesharer.share()
		self.ids.link.text = url

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
