from datetime import datetime
import pytz

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

class GradeDTO:
    def __init__(self, id, student_id, course_id, grade, semester, created_at, updated_at, 
                 course_name, student_firstname, student_lastname):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade
        self.semester = semester
        self.created_at = created_at
        self.updated_at = updated_at
        self.course_name = course_name
        self.student_firstname = student_firstname
        self.student_lastname = student_lastname

    def full_name(self):
        return f"{self.student_firstname} {self.student_lastname}"

    def to_dict(self):
        return {
            'id': self.id,
            'grade': self.grade,
            'semester': self.semester,
            'course_name': self.course_name,
            'student_name': self.full_name(),
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }
