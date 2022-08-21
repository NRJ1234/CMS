from app.service import db

def get_all_teachers():
    session = db.initiate_global_mysql_session()
    query = "SELECT * FROM teachers;"
    session['cursor'].execute(query)
    res = session['cursor'].fetchall()
    return res

def insert_teacher(data):
    session = db.initiate_global_mysql_session()
    query = "INSERT INTO teachers (first_name, last_name) VALUES (%s, %s);"
    session['cursor'].execute(query, (data['first_name'], data['last_name']))
    db.commit_mysql_session(session)

def view_classes_today(data):
    session = db.initiate_global_mysql_session()
    query = "SELECT c.subject, t.start_time, t.end_time FROM classes c JOIN timetable t ON c.id = t.class_id \
        WHERE date(t.start_time) = curdate() AND date(t.end_time) = curdate() AND c.teacher_id = %s;"
    session['cursor'].execute(query, (data['teacher_id'],))
    res = session['cursor'].fetchall()
    return res