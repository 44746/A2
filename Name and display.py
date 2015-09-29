from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from name_widget import *
from display_widget import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ##Create widgets
        self.name_widget=NameWidget()
        self.display_widget = DisplayWidget()
        ##Create stack layout
        self.stack = QStackedLayout()
        ##add widgets to stack
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.display_widget)
        ##add stack to central widget
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)
        ##Connections
        self.name_widget.NameEntered.connect(self.name_provided)

    def name_provided(self):
        self.stack.setCurrentIndex(1)
        name = self.name_widget.username.text()
        self.display_widget.label.setText("Hello {0}".format(name))

        self.display_widget.BackPushed.connect(self.loop)

    def loop(self):
        self.name_widget.username.clear()
        self.stack.setCurrentIndex(0)
       

if __name__ == "__main__":
    ##Create new application
    app = QApplication(sys.argv)
    ##instantiate window
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
