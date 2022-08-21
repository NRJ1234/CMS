from app.service import db

def get_all_classes():
    session = db.initiate_global_mysql_session()
    query = "SELECT * FROM classes;"
    session['cursor'].execute(query)
    res = session['cursor'].fetchall()
    return res

def add_class(data):
    session = db.initiate_global_mysql_session()
    query = "INSERT INTO classes (subject, teacher_id) VALUES (%s, %s);"
    session['cursor'].execute(query, (data['subject'], data['teacher_id']))
    db.commit_mysql_session(session)

def assign_students(data):
    session = db.initiate_global_mysql_session()
    query = "INSERT IGNORE INTO class_student_mapping (class_id, student_id) VALUES (%s, %s);"
    for element in data['student_id_list']:
        session['cursor'].execute(query, (data['class_id'], element))
    db.commit_mysql_session(session)

def schedule_class(data):
    session = db.initiate_global_mysql_session()
    query = "INSERT INTO timetable (class_id, start_time, end_time) VALUES (%s, %s, %s);"
    for element in data:
        session['cursor'].execute(query, (element['class_id'], element['start_time'], element['end_time']))
    db.commit_mysql_session(session)