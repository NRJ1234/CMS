from flask import jsonify, request
from app.controllers import class_controller as cc
from app.repository import classes as cl

@cc.route('/classes/list', methods=['GET'])
def classes():
    """ Output: Returns list of all classes """
    try:
        res = cl.get_all_classes()
        return jsonify(res), 200
    except Exception as e:
        return jsonify([]), 500

@cc.route("/classes/add_class", methods=['POST'])
def add_class():
    """ 
    Input: {subject: <string>, teacher_id: <integer>}
    Output: Success/Error message
    """
    try:
        print(request.get_json())
        cl.add_class(request.get_json())
        return "Success", 200
    except Exception as e:
        return str(e), 500

@cc.route("/classes/assign_students", methods=['POST'])
def assign_students():
    """
    Input: {class_id: <integer>, student_id_list: <List of integers>}
    Output: Success/Error message
    """
    try:
        print(request.get_json())
        cl.assign_students(request.get_json())
        return "Success", 200
    except Exception as e:
        return str(e), 500

@cc.route("/classes/schedule_class", methods=['POST'])
def schedule_class():
    """
    Input: [{class_id: <integer>, start_time: <timestamp>, end_time: <timestamp>}]
    Output: Success/Error message
    """
    try:
        print(request.get_json())
        cl.schedule_class(request.get_json())
        return "Success", 200
    except Exception as e:
        return str(e), 500