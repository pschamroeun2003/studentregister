from datetime import datetime
import pytz

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

class InstructorDTO:
    def __init__(self, id, firstname, lastname, dob, gender, email, phone, department, created_at, updated_at):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone = phone
        self.department = department
        self.created_at = created_at
        self.updated_at = updated_at

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def to_dict(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'full_name': self.full_name(),
            'dob': self.dob.strftime('%Y-%m-%d') if self.dob else None,
            'gender': self.gender,
            'email': self.email,
            'phone': self.phone,
            'department': self.department,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }
