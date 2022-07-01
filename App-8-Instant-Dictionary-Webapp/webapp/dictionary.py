import justpy as jp
import requests

from webapp import layout
from dictionary_func import DictionaryFunc
from webapp import page


class Dictionary(page.Page):
	path = '/dictionary'

	@classmethod
	def serve(cls, req):
		wp = jp.QuasarPage(tailwind=True)

		# Default layout
		lo = layout.DefaultLayout(a=wp)

		# Main content in container
		container = jp.QPageContainer(a=lo)
		div = jp.Div(a=container, classes='bg-grey-200 h-screen p-2')
		jp.Div(a=div, text='Instant English Dictionary', classes='text-4xl m-2')
		jp.Div(a=div, text='Get the definition of any English word instantly as you type!', classes='text-lg')

		input_div = jp.Div(a=div, classes='grid grid-cols-2')

		output_div = jp.Div(a=div, classes='m-2 p-2 text-lg border-2 h-40')

		input_box = jp.Input(a=input_div, placeholder='Type in a word here...', outputdiv=output_div,
		         classes='m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 '
		                 'focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4')
		input_box.on('input', cls.get_definition)
		# jp.Button(a=input_div, text='Get Definition', classes='border-2 text-gray-500',
		#           click=cls.get_definition, inputbox=input_box, outputdiv=output_div)

		return wp

	@staticmethod
	def get_definition(widget, msg):
		"""
		Gets the definition(s) of a word.
		"""
		dictionary = DictionaryFunc()
		term = widget.value
		# definitions = dictionary.get_definition(term)  # Direct access
		req = requests.get(f'http://127.0.0.1:8001/api?w={term}') # Use API from App9
		definitions = req.json()['definition']
		widget.outputdiv.text = " ".join(definitions)


if __name__ == "__main__":
	jp.Route(Dictionary.path, Dictionary.serve)
	jp.justpy()
