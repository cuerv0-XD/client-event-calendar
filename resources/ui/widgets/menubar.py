from PyQt5 import QtCore, QtGui, QtWidgets


class MenuBar(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.horizontalLayoutWidget = QtWidgets.QWidget()
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 401, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.homeButton = QtWidgets.QPushButton("HOME", self.horizontalLayoutWidget)
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout.addWidget(self.homeButton)

        self.calendarButton = QtWidgets.QPushButton("CALENDAR",self.horizontalLayoutWidget)
        self.calendarButton.setObjectName("calendarButton")
        self.horizontalLayout.addWidget(self.calendarButton)

        self.clientsButton = QtWidgets.QPushButton("CLIENTS", self.horizontalLayoutWidget)
        self.clientsButton.setObjectName("clientsButton")
        self.horizontalLayout.addWidget(self.clientsButton)

        self.settingsButton = QtWidgets.QPushButton("SETTINGS", self.horizontalLayoutWidget)
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout.addWidget(self.settingsButton)

        self.layout.addWidget(self.horizontalLayoutWidget)