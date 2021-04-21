from PyQt5 import QtWidgets
class EchoText(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = QtWidgets.QGridLayout()
		self.setLayout(self.layout)

		self.textbox = QtWidgets.QLineEdit()
		self.echo_label = QtWidgets.QLabel('')

		self.textbox.textChanged.connect(self.textbox_text_changed)

		self.layout.addWidget(self.textbox, 0, 0)
		self.layout.addWidget(self.echo_label, 1, 0)

	def textbox_text_changed(self):
		self.echo_label.setText(self.textbox.text())