from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


from filesharer import FileSharer

# Load the kivy config file
Builder.load_file("frontend.kv")


class CameraScreen(Screen):
	"""
	The camera screen of the app: one screen class per screen required.
	"""
	def start(self):
		self.ids.camera.play = True
		self.ids.camera_button.text = 'Stop Camera'
		self.ids.camera.texture = self.ids.camera._camera.texture

	def stop(self):
		self.ids.camera.play = False
		self.ids.camera_button.text = 'Start Camera'
		self.ids.camera.texture = None

	def capture(self):
		pass


class ImageScreen(Screen):
	"""
	The image screen of the app: one screen class per screen required.
	"""
	pass


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
