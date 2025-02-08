from datetime import datetime
import pytz 
CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')
class StudentDTO:
    def __init__(self, id, firstname, lastname, dob, gender, email, phone=None, address=None, created_at=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone = phone
        self.address = address
        self.created_at = created_at
    def to_dict(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'dob': self.dob.strftime('%Y-%m-%d'),
            'gender': self.gender,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'created_at': self.created_at
        }
