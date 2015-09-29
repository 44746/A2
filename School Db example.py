import sqlite3

def execute_sql(db_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

if __name__ == "__main__":
    db_name= "School.db"
    sql = """create table teacher
             (teacherID integer,
             name text,
             primary Key(teacherID))"""
    execute_sql(db_name, sql)
    
    sql = """create table student
             (studentID integer,
             name text,
             teacherID,
             primary Key(studentID))"""

    execute_sql(db_name, sql)
    
             
