from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

# Define the timezone for Cambodia
CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

# Function to get the current time in Cambodia timezone
def get_current_time():
    return datetime.now(CAMBODIA_TZ)

# Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=get_current_time, onupdate=get_current_time, nullable=False)

    def __repr__(self):
        return f'<Student {self.firstname} {self.lastname}>'

# Course Model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(), nullable=False)
    code = db.Column(db.String(), nullable=True)
    credits = db.Column(db.String(), nullable=True)
    department = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=get_current_time, onupdate=get_current_time, nullable=False)

    def __repr__(self):
        return f'<Course {self.course_name} ({self.code})>'
