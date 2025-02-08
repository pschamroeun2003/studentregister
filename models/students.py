from extensions import db
from datetime import datetime
import pytz
# Cambodia Timezone
CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')
def get_current_time():
    """Return the current time in Cambodia timezone."""
    return datetime.now(CAMBODIA_TZ)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime, default=get_current_time, onupdate=get_current_time, nullable=False)

    def __repr__(self):
        return f"<Student {self.firstname} {self.lastname}>"
