from extensions import db
from datetime import datetime
import pytz

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')
def get_current_time():
    return datetime.now(CAMBODIA_TZ)

class CourseSchedule(db.Model):
    __tablename__ = 'course_schedule'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'), nullable=False)
    day_of_week = db.Column(db.String(10), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    room_number = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=get_current_time, onupdate=get_current_time, nullable=False)
    course = db.relationship('Course', backref='course_schedules', lazy=True)
    instructor = db.relationship('Instructor', backref='course_schedules', lazy=True)
    def __repr__(self):
        return f"<CourseSchedule id={self.id}, course_id={self.course_id}, instructor_id={self.instructor_id}, day_of_week={self.day_of_week}>"
