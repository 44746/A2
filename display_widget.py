from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DisplayWidget(QWidget):
    BackPushed = pyqtSignal()
    def __init__(self):
        super().__init__()

       
        self.label = QLabel()
        self.button = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        
        self.button.clicked.connect(self.back_pushed)

    def back_pushed(self):
        self.BackPushed.emit()


