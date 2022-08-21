from flask import Flask
from app import controllers as ctr

def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(ctr.student_controller)
    flask_app.register_blueprint(ctr.teacher_controller)
    flask_app.register_blueprint(ctr.class_controller)
    return flask_app