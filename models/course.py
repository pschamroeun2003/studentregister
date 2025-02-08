from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
db = SQLAlchemy()
CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')
def get_current_time():
    return datetime.now(CAMBODIA_TZ)



class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(),nullable=False)
    code = db.Column(db.String(),nullable=True)
    credits = db.Column(db.String(),nullable=True)
    department = db.Column(db.String(),nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=get_current_time, onupdate=get_current_time, nullable=False)
    def __repr__(self):
        return f'<Student {self.firstname} {self.lastname}>'
