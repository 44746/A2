from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NameWidget(QWidget):
    NameEntered = pyqtSignal()
    IDEntered = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.username = QLineEdit()
        self.label = QLabel("Please enter your Name: ")
        self.ID = QLineEdit()
        self.label2 = QLabel("Please enter your ID: ")
        

        self.add= QPushButton("Add")
        self.delete= QPushButton("Delete")


        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.ID)
        self.layout.addWidget(self.add)
        self.layout.addWidget(self.delete)

        self.setLayout(self.layout)

        self.add.clicked.connect(self.add_pushed)
        self.delete.clicked.connect(self.delete_pushed)

    def delete_pushed(self):
        pass

    def add_pushed(self):
        name = self.username.text()
        self.NameEntered.emit()
        ID = self.ID.text()
        self.IDEntered.emit()
