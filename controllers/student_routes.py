from flask import Blueprint, request, jsonify
from models.students import  Student ,db
from datetime import datetime
from DTO.StudentDTO import StudentDTO
import re
student_bp = Blueprint('student', __name__, url_prefix='/api/students')

def is_valid_email(email):
    """Validate the email format using regex."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@student_bp.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    required_fields = ['firstname', 'lastname', 'dob', 'gender', 'email']
    if not data or not all(key in data for key in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    if not is_valid_email(data['email']):
        return jsonify({"message": "Invalid email format"}), 400
    try:
        dob = datetime.strptime(data['dob'], '%Y-%m-%d')
        new_student = Student(
            firstname=data['firstname'],
            lastname=data['lastname'],
            dob=dob,
            gender=data['gender'],
            email=data['email'],
            phone=data.get('phone', None),
            address=data.get('address', None)
        )
        db.session.add(new_student)
        db.session.commit()
        student_dto = StudentDTO(
            id=new_student.id,
            firstname=new_student.firstname,
            lastname=new_student.lastname,
            dob=new_student.dob,
            gender=new_student.gender,
            email=new_student.email,
            phone=new_student.phone,
            address=new_student.address,
            created_at = new_student.created_at
        )
        return jsonify(student_dto.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
    

@student_bp.route('/student', methods=['GET'])
def get_all_students():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    if per_page < 1 or per_page > 100:
        return jsonify({"message": "'per_page' must be between 1 and 100"}), 400
    students = Student.query.paginate(page=page, per_page=per_page, error_out=False)
    student_dtos = [StudentDTO(
        id=student.id,
        firstname=student.firstname,
        lastname=student.lastname,
        dob=student.dob,
        gender=student.gender,
        email=student.email,
        phone=student.phone,
        address=student.address,
        created_at = student.created_at
    ).to_dict() for student in students.items]
    pagination = {
        'page': students.page,
        'per_page': students.per_page,
        'total_items': students.total,
        'total_pages': students.pages,
    }
    if students.has_next:
        next_page_link = f"/api/students/student?page={students.page + 1}&per_page={students.per_page}"
    else:
        next_page_link = None
    if students.has_prev:
        prev_page_link = f"/api/students/student?page={students.page - 1}&per_page={students.per_page}"
    else:
        prev_page_link = None
    return jsonify({
        'pagination': pagination,
        'students': student_dtos,
        'next_page_link': next_page_link,
        'prev_page_link': prev_page_link
    })



@student_bp.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get(id)
    if not student:
        return jsonify({"message": "Student not found"}), 404
    if 'firstname' in data:
        student.firstname = data['firstname']
    if 'lastname' in data:
        student.lastname = data['lastname']
    if 'dob' in data:
        try:
            student.dob = datetime.strptime(data['dob'], '%Y-%m-%d')
        except ValueError:
            return jsonify({"message": "Invalid date format, should be YYYY-MM-DD"}), 400
    if 'gender' in data:
        student.gender = data['gender']
    if 'email' in data:
        if not is_valid_email(data['email']):
            return jsonify({"message": "Invalid email format"}), 400
        student.email = data['email']
    if 'phone' in data:
        student.phone = data['phone']
    if 'address' in data:
        student.address = data['address']
    db.session.commit()
    student_dto = StudentDTO(
        id=student.id,
        firstname=student.firstname,
        lastname=student.lastname,
        dob=student.dob,
        gender=student.gender,
        email=student.email,
        phone=student.phone,
        address=student.address
    )
    return jsonify(student_dto.to_dict())

@student_bp.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    
    if student:
        student_dto = StudentDTO(
            id=student.id,
            firstname=student.firstname,
            lastname=student.lastname,
            dob=student.dob,
            gender=student.gender,
            email=student.email,
            phone=student.phone,
            address=student.address
        )
        return jsonify(student_dto.to_dict())
    else:
        return jsonify({"message": "Student not found"}), 404
    
@student_bp.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    
    if not student:
        return jsonify({"message": "Student not found"}), 404
    
    # Delete the student and commit
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"})
