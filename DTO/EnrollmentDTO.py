from datetime import datetime
import pytz

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

class EnrollmentDTO:
    def __init__(self, id, student_id, course_id, status, firstname, lastname, created_at=None, updated_at=None):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
        self.status = status
        self.firstname = firstname
        self.lastname = lastname
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'status': self.status.name if self.status else None,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }
