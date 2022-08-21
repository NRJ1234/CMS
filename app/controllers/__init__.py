from flask import Blueprint, jsonify

student_controller =  Blueprint('students', __name__)
teacher_controller =  Blueprint('teachers', __name__)
class_controller =  Blueprint('classes', __name__)

from app.controllers import students
from app.controllers import teachers
from app.controllers import classes