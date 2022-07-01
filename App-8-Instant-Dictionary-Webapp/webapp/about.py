import justpy as jp

from webapp import layout
from webapp import page


class About(page.Page):
	path = '/about'

	def serve(self):
		wp = jp.QuasarPage(tailwind=True)

		# Default layout
		lo = layout.DefaultLayout(a=wp)

		# Main content in container
		container = jp.QPageContainer(a=lo)
		div = jp.Div(a=container, classes='bg-grey-200 h-screen p-2')
		jp.Div(a=div, text='This is the About page!', classes='text-4xl m-2')
		jp.Div(a=div, text='Content', classes='text-lg')

		return wp


if __name__ == "__main__":
	jp.Route(About.path, About.serve)
	jp.justpy()
