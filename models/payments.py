from extensions import db
from datetime import datetime
from ENUM.PaymentMethod import PaymentMethod
import pytz
CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')
def get_current_time():
    return datetime.now(CAMBODIA_TZ)
class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    amount = db.Column(db.Float)
    payment_method = db.Column(db.Enum(PaymentMethod), nullable=False)
    payment_date = db.Column(db.DateTime(timezone=True), default=get_current_time, nullable=False)
    transaction_ref = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=get_current_time, nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=get_current_time, onupdate=get_current_time, nullable=False)
    student = db.relationship('Student', backref='payments', lazy=True)
    course = db.relationship('Course', backref='payments', lazy=True)
    def __repr__(self):
        return f'<Payment {self.student.firstname} {self.student.lastname} for {self.course.course_name}>' if self.student and self.course else '<Payment>'
