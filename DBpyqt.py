from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

from name_widgetDB import *
from display_widgetDB import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ##Create widgets
        self.name_widgetDB=NameWidget()
        self.display_widgetDB = DisplayWidget()
        ##Create stack layout
        self.stack = QStackedLayout()
        ##add widgets to stack
        self.stack.addWidget(self.name_widgetDB)
        self.stack.addWidget(self.display_widgetDB)
        ##add stack to central widget
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)
        ##Connections
        self.name_widgetDB.NameEntered.connect(self.data_provided)
        
        
        

    def data_provided(self):
        self.stack.setCurrentIndex(1)
        name = self.name_widgetDB.username.text()
        ID = self.name_widgetDB.ID.text()
        self.display_widgetDB.label.setText("Name:{0} ID:{1}".format(name,ID))
        
        
        
        self.display_widgetDB.BackPushed.connect(self.loop)
        
    def loop(self):
        self.name_widgetDB.username.clear()
        self.name_widgetDB.ID.clear()
        self.stack.setCurrentIndex(0)

class database():
    def __init__(self):
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        db_name= ""
        sql = """create table teacher
             (TeacherID integer,
             Name text,
             primary Key(TeacherID))"""
        execute_sql(db_name, sql)
    def createData(self):
        sql = "insert into Teacher.db (TeacherID, Name) values"



if __name__ == "__main__":
    ##Create new application
    app = QApplication(sys.argv)
    ##instantiate window
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
