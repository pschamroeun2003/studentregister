from extensions import db
from datetime import datetime
import pytz

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

# Function to get the current time in Cambodia timezone
def get_current_time():
    return datetime.now(CAMBODIA_TZ)

class Instructor(db.Model):
    __tablename__ = 'instructors'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    department = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime, default=get_current_time, onupdate=get_current_time, nullable=False)
    def __repr__(self):
        return f"<Instructor id={self.id}, firstname={self.firstname}, lastname={self.lastname}, email={self.email}>"
