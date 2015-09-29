import sqlite3

class database():
    def __init__(self):

        
        sql = """create table teacher
             (TeacherID integer,
             Name text,
             primary Key(TeacherID))"""
        self.execute_sql(sql)

    def execute_sql(self,sql):
        db_name= "Teacher.db"
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()

        
    def createData(self):
        sql = "insert into Teacher.db (TeacherID, Name) values"
        self.execute_sql(sql)


if __name__ == "__main__":
    my_database = database()
    my_database.createData()
