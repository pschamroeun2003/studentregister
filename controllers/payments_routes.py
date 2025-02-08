from flask import Blueprint, request, jsonify
from models.payments import Payment
from extensions import db
from datetime import datetime
from ENUM.PaymentMethod import PaymentMethod 
from DTO.PaymentDTO import PaymentDTO
payments_bp = Blueprint('payments', __name__, url_prefix='/api/payments')

@payments_bp.route('/payment', methods=['POST'])
def add_payment():
    data = request.get_json()
    required_fields = ['student_id', 'course_id', 'amount', 'payment_method', 'transaction_ref']
    if not data or not all(key in data for key in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    
    try:
        new_payment = Payment(
            student_id=data['student_id'],
            course_id=data['course_id'],
            amount=data['amount'],
            transaction_ref=data['transaction_ref'],
            payment_method=PaymentMethod[data['payment_method']],
            payment_date=datetime.now(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(new_payment)
        db.session.commit()
        student_name = f"{new_payment.student.firstname} {new_payment.student.lastname}" if new_payment.student else None
        course_name = new_payment.course.course_name if new_payment.course else None
        payment_dto = PaymentDTO(
            id=new_payment.id,
            student_id=new_payment.student_id,
            course_id=new_payment.course_id,
            amount=new_payment.amount,
            payment_method=new_payment.payment_method.name,
            payment_date=new_payment.payment_date,
            transaction_ref=new_payment.transaction_ref,
            created_at=new_payment.created_at,
            updated_at=new_payment.updated_at,
            student_name=student_name,
            course_name=course_name
        )
        return jsonify({"data":payment_dto.to_dict() , "status":"success"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500



@payments_bp.route('/payment/<int:id>', methods=['GET'])
def get_payment(id):
    payment = Payment.query.get(id)
    if not payment:
        return jsonify({"message": "Payment not found"}), 404
    student_name = f"{payment.student.firstname} {payment.student.lastname}" if payment.student else None
    course_name = payment.course.course_name if payment.course else None
    payment_dto = PaymentDTO(
        id=payment.id,
        student_id=payment.student_id,
        course_id=payment.course_id,
        amount=payment.amount,
        payment_method=payment.payment_method.name,
        payment_date=payment.payment_date,
        transaction_ref=payment.transaction_ref,
        created_at=payment.created_at,
        updated_at=payment.updated_at,
        student_name=student_name,
        course_name=course_name
    )
    return jsonify({"data":payment_dto.to_dict()}), 200

@payments_bp.route('/payment/<int:id>', methods=['PUT'])
def update_payment(id):
    payment = Payment.query.get(id)
    if not payment:
        return jsonify({"message": "Payment not found"}), 404
    data = request.get_json()
    if 'amount' in data:
        payment.amount = data['amount']
    if 'payment_method' in data:
        payment.payment_method = PaymentMethod[data['payment_method']]
    if 'transaction_ref' in data:
        payment.transaction_ref = data['transaction_ref']
    payment.updated_at = datetime.now()
    try:
        db.session.commit()
        student_name = f"{payment.student.firstname} {payment.student.lastname}" if payment.student else None
        course_name = payment.course.course_name if payment.course else None
        payment_dto = PaymentDTO(
            id=payment.id,
            student_id=payment.student_id,
            course_id=payment.course_id,
            amount=payment.amount,
            payment_method=payment.payment_method.name,
            payment_date=payment.payment_date,
            transaction_ref=payment.transaction_ref,
            created_at=payment.created_at,
            updated_at=payment.updated_at,
            student_name=student_name,
            course_name=course_name
        )
        return jsonify({"data":payment_dto.to_dict() , "status":"success"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500

    


