import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from resources.ui.widgets import echotext, calendar, menubar, scrollview

class MainWindow(QtWidgets.QMainWindow):

	def __init__(self, parent = None):
		super().__init__(parent)
		self.init_gui()

	def init_gui(self):
		self.window = QtWidgets.QWidget()
		self.layout = QtWidgets.QGridLayout()
		self.setCentralWidget(self.window)
		self.window.setLayout(self.layout)
		
		self.init_menubar()

	def init_echotext(self):
		self.echotext_widget = echotext.EchoText()
		self.layout.addWidget(self.echotext_widget)

	def init_calendar(self):
		self.init_menubar()
		self.calendar_widget = calendar.Calendar()
		self.layout.addWidget(self.calendar_widget)
	
	def init_clients(self):
		self.init_menubar()
		self.scrollview_widget = scrollview.ScrollView()
		self.layout.addWidget(self.scrollview_widget)

	def init_menubar(self):
		self.clear_widgets()
		self.menubar_widget = menubar.MenuBar()
		self.layout.addWidget(self.menubar_widget)
		self.menubar_widget.homeButton.clicked.connect(self.init_menubar)
		self.menubar_widget.calendarButton.clicked.connect(self.init_calendar)
		self.menubar_widget.clientsButton.clicked.connect(self.init_clients)

	def clear_widgets(self):
		for i in reversed(range(self.layout.count())):
			self.layout.itemAt(i).widget().setParent(None)

if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	win = MainWindow()
	win.showMaximized()

	sys.exit(app.exec_())