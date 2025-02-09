from flask import Flask, jsonify
from extensions import db
from controllers.student_routes import student_bp
from controllers.course_routes import course_bp
from controllers.enrollment_routes import enrollment_bp
from controllers.grade_routes import grade_bp
from controllers.instructor_routes import instructors_bp
from controllers.courseschedules_routes import courseschedules_bp
from controllers.payments_routes import payments_bp
from flask_cors import CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register_student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

CORS(app)

# Register blueprints for routes
app.register_blueprint(student_bp)
app.register_blueprint(course_bp)
app.register_blueprint(enrollment_bp)
app.register_blueprint(grade_bp)
app.register_blueprint(instructors_bp)
app.register_blueprint(courseschedules_bp)
app.register_blueprint(payments_bp)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Student API"})

if __name__ == '__main__':
    with app.app_context():
         db.create_all()  # Recreate tables
         print("Database and tables created.")
    app.run(host='0.0.0.0', port=5000, debug=True)

