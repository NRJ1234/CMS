from flask import jsonify, request
from app.controllers import teacher_controller as tc
from app.repository import teachers as te

@tc.route('/teachers', methods=['GET'])
def teachers():
    """ Output: Returns list of all teachers """
    try:
        res = te.get_all_teachers()
        return jsonify(res), 200
    except Exception as e:
        return jsonify([]), 500

@tc.route("/teachers/insert", methods=['POST'])
def insert_teacher():
    """
    Input: {teacher_id: <integer>} 
    Output: Success/Error message
    """
    try:
        print(request.get_json())
        te.insert_teacher(request.get_json())
        return "Success", 200
    except Exception as e:
        return str(e), 500

@tc.route("/teachers/view_classes_today", methods=['POST'])
def view_classes_today():
    """
    Input: {teacher_id: <integer>} 
    Output: [{subject: <string>, start_time: <timestamp>, end_time: <timestamp>}]
    """
    try:
        print(request.get_json())
        res = te.view_classes_today(request.get_json())
        return jsonify(res), 200
    except Exception as e:
        return str(e), 500