from extensions import db
from datetime import datetime
import pytz

# Cambodia Timezone
CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

def get_current_time():
    return datetime.now(CAMBODIA_TZ)

class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False) 
    grade = db.Column(db.String, nullable=False)
    semester = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime, default=get_current_time, onupdate=get_current_time, nullable=False)
    student = db.relationship('Student', backref=db.backref('grades', lazy=True))
    course = db.relationship('Course', backref=db.backref('grades', lazy=True))
    def __repr__(self):
        return f"<Grade student_id={self.student_id}, course_id={self.course_id}, grade={self.grade}>"
