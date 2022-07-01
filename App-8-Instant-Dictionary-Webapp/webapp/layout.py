import justpy as jp

class DefaultLayout(jp.QLayout):

	def __init__(self, view="hHh lpR fFf", **kwargs):
		super().__init__(view=view, **kwargs)

		# Header
		header = jp.QHeader(a=self, elevated=True, clasess="bg-primary text-white")

		## Toolbar
		toolbar = jp.QToolbar(a=header)

		# Drawer
		drawer = jp.QDrawer(a=self, show_if_above=True, v_model="leftDrawerOpen", side="left", bordered=True)
		jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
		        click=self.move_drawer, drawer=drawer)
		jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')

		scroller = jp.QScrollArea(a=drawer, classes='fit')
		qlist = jp.QList(a=scroller)
		a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
		jp.A(a=qlist, text='Home', href='/', classes=a_classes)
		jp.Br(a=qlist)
		jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
		jp.Br(a=qlist)
		jp.A(a=qlist, text='About', href='/about', classes=a_classes)
		jp.Br(a=qlist)

	@staticmethod
	def move_drawer(widget, msg):
		widget.drawer.value = not widget.drawer.value
