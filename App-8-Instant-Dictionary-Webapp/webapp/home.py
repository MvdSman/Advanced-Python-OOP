import justpy as jp

from webapp import layout


class Home:
	path = '/'

	@classmethod
	def serve(cls):
		wp = jp.QuasarPage(tailwind=True)

		# Default layout
		lo = layout.DefaultLayout(a=wp)

		# Main content in container
		container = jp.QPageContainer(a=lo)
		div = jp.Div(a=container, classes='bg-grey-200 h-screen p-2')
		jp.Div(a=div, text='This is the Home page!', classes='text-4xl m-2')
		jp.Div(a=div, text='Content', classes='text-lg')

		return wp


if __name__ == "__main__":
	jp.Route(Home.path, Home.serve)
	jp.justpy()
