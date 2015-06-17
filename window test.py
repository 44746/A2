from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from name_widget import *
from display_widget import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.name_widget=NameWidget()
        self.display_widget = DisplayWidget()

        self.setCentralWidget(self.name_widget)
        self.name_widget.NameEntered.connect(self.name_provided)

    def name_provided(self):
        self.setCentralWidget(self.display_widget)
        name = self.name_widget.username.text()
        self.display_widget.label.setText(name)

        self.display_widget.BackPushed.connect(self.asdf)

    def asdf(self):
        print("qwerty")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
