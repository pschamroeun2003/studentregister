from datetime import datetime
import pytz

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

class PaymentDTO:
    def __init__(self, id, student_id, course_id, amount, payment_method, payment_date, transaction_ref, created_at, updated_at, student_name=None, course_name=None):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.student_name = student_name
        self.course_name = course_name
        self.transaction_ref = transaction_ref

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'amount': self.amount,
            'payment_method': self.payment_method,
            'payment_date': self.payment_date.strftime('%Y-%m-%d %H:%M:%S') if self.payment_date else None,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None,
            'student_name': self.student_name,
            'course_name': self.course_name,
            'transaction_ref':self.transaction_ref
        }
