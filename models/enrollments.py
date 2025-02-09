from extensions import db
from datetime import datetime
import pytz
from ENUM.enrollment_status import EnrollmentStatus
from models.courses import Course  # Ensure this import exists
from models.students import Student  # Ensure this import exists

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

def get_current_time():
    return datetime.now(CAMBODIA_TZ)

class Enrollment(db.Model):
    __tablename__ = "enrollments"  # Ensure table names match foreign keys

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=True)
    status = db.Column(db.Enum(EnrollmentStatus), nullable=False, default=EnrollmentStatus.ENROLLED)
    created_at = db.Column(db.DateTime(timezone=True), default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=get_current_time, onupdate=get_current_time, nullable=False)

    student = db.relationship("Student", backref="enrollments", lazy=True)
    course = db.relationship("Course", backref="enrollments", lazy=True)

    def __repr__(self):
        return f'<Enrollment {self.student.firstname} {self.student.lastname} in {self.course.course_name}>'
