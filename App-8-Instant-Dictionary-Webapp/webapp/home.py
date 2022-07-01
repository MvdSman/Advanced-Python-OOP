import justpy as jp


class Home:
	path = '/'

	def serve(self):
		wp = jp.QuasarPage(tailwind=True)
		div = jp.Div(a=wp, classes='bg-grey-200 h-screen')
		jp.Div(a=div, text='This is the Home page!', classes='text-4xl m-2')
		jp.Div(a=div, text='Content', classes='text-lg')

		return wp


if __name__ == "__main__":
	jp.Route(Home.path, Home.serve)
	jp.justpy()