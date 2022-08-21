from app.service import db

def get_all_students():
    session = db.initiate_global_mysql_session()
    query = "SELECT * FROM students;"
    session['cursor'].execute(query)
    res = session['cursor'].fetchall()
    return res

def insert_student(data):
    session = db.initiate_global_mysql_session()
    query = "INSERT INTO students (first_name, last_name) VALUES (%s, %s);"
    session['cursor'].execute(query, (data['first_name'], data['last_name']))
    db.commit_mysql_session(session)

def view_classes_today(data):
    session = db.initiate_global_mysql_session()
    query = "SELECT c.subject, t.start_time, t.end_time FROM classes c \
        JOIN timetable t ON c.id = t.class_id \
        JOIN class_student_mapping csm ON csm.class_id = c.id \
        WHERE date(t.start_time) = curdate() AND date(t.end_time) = curdate() AND csm.student_id = %s;"
    session['cursor'].execute(query, (data['student_id'],))
    res = session['cursor'].fetchall()
    return res