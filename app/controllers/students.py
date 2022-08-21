from flask import jsonify, request
from app.controllers import student_controller as sc
from app.repository import students as st

@sc.route('/students/list', methods=['GET'])
def list_students():
    """ Output: Returns list of all students """
    try:
        res = st.get_all_students()
        return jsonify(res), 200
    except Exception as e:
        return jsonify([]), 500

@sc.route("/students/insert", methods=['POST'])
def insert_student():
    """
    Input: {student_id: <integer>} 
    Output: Success/Error message
    """
    try:
        print(request.get_json())
        st.insert_student(request.get_json())
        return "Success", 200
    except Exception as e:
        return str(e), 500

@sc.route("/students/view_classes_today", methods=['POST'])
def view_classes_today():
    """
    Input: {student_id: <integer>} 
    Output: [{subject: <string>, start_time: <timestamp>, end_time: <timestamp>}]
    """
    try:
        print(request.get_json())
        res = st.view_classes_today(request.get_json())
        return jsonify(res), 200
    except Exception as e:
        return str(e), 500