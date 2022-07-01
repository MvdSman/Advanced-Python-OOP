import justpy as jp


class Docs:
	path = '/'

	def serve(self):
		wp = jp.WebPage()

		div = jp.Div(a=wp, classes='bg-grey-200 h-screen p-2')
		jp.Div(a=div, text='Instant Dictionary API', classes='text-4xl m-2')
		jp.Div(a=div, text='Get definitions of words:', classes='text-lg')
		jp.Hr(a=div)
		jp.Div(a=div, text='http://127.0.0.1:8001/api?w=moon', classes='text-lg')
		jp.Hr(a=div)
		jp.Div(
			a=div,
			text='{"word": "moon", '
                 '"definition": ["A natural satellite of a planet.", '
                 '"A month, particularly a lunar month (approximately 28 days).", '
                 '"To fuss over adoringly or with great affection.", '
                 '"Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).", '
                 '"To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]}'
		)

		return wp


if __name__ == "__main__":
	jp.Route(Docs.path, Docs.serve)
	jp.justpy(port=8001)
