from datetime import datetime
import pytz

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

class CourseDTO:
    def __init__(self, id, course_name, code=None, credits=None, department=None, created_at=None , updated_at = None):
        self.id = id
        self.course_name = course_name
        self.code = code
        self.credits = credits
        self.department = department
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            'id': self.id,
            'course_name': self.course_name,
            'code': self.code,
            'credits': self.credits,
            'department': self.department,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }
