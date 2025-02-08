from flask import Blueprint, request, jsonify
from models.instructors import Instructor
from extensions import db
from DTO.InstructorDTO import InstructorDTO
from datetime import datetime
instructors_bp = Blueprint('instructors', __name__, url_prefix='/api/instructors')
@instructors_bp.route('/instructor', methods=['POST'])
def add_instructor():
    data = request.get_json()
    required_fields = ['firstname', 'lastname', 'dob', 'gender', 'email']
    if not data or not all(key in data for key in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    try:
        new_instructor = Instructor(
            firstname=data['firstname'],
            lastname=data['lastname'],
            dob=datetime.strptime(data['dob'], '%Y-%m-%d'),
            gender=data['gender'],
            email=data['email'],
            phone=data.get('phone', None),
            department=data.get('department', None),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(new_instructor)
        db.session.commit()
        instructor_dto = InstructorDTO(
            id=new_instructor.id,
            firstname=new_instructor.firstname,
            lastname=new_instructor.lastname,
            dob=new_instructor.dob,
            gender=new_instructor.gender,
            email=new_instructor.email,
            phone=new_instructor.phone,
            department=new_instructor.department,
            created_at=new_instructor.created_at,
            updated_at=new_instructor.updated_at
        )
        return jsonify(instructor_dto.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
    
@instructors_bp.route('/instructor', methods=['GET'])
def get_all_instructors():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        instructors = Instructor.query.paginate(page=page, per_page=per_page, error_out=False)
        instructor_dtos = [
            InstructorDTO(
                id=instructor.id,
                firstname=instructor.firstname,
                lastname=instructor.lastname,
                dob=instructor.dob,
                gender=instructor.gender,
                email=instructor.email,
                phone=instructor.phone,
                department=instructor.department,
                created_at=instructor.created_at,
                updated_at=instructor.updated_at
            ) for instructor in instructors.items
        ]
        pagination = {
            "page": instructors.page,
            "per_page": instructors.per_page,
            "total": instructors.total,
            "pages": instructors.pages
        }
        next_page_link = f"/api/instructors/instructor?page={instructors.page + 1}&per_page={instructors.per_page}" if instructors.has_next else None
        prev_page_link = f"/api/instructors/instructor?page={instructors.page - 1}&per_page={instructors.per_page}" if instructors.has_prev else None
        return jsonify({
            "pagination": pagination,
            "data": [instructor.to_dict() for instructor in instructor_dtos],
            "next_page_link": next_page_link,
            "prev_page_link": prev_page_link,
        }), 200
    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
    
@instructors_bp.route('/instructor/<int:id>', methods=['GET'])
def get_instructor_by_id(id):
    try:
        instructor = Instructor.query.get(id)
        if not instructor:
            return jsonify({"message": "Instructor not found"}), 404
        
        instructor_dto = InstructorDTO(
            id=instructor.id,
            firstname=instructor.firstname,
            lastname=instructor.lastname,
            dob=instructor.dob,
            gender=instructor.gender,
            email=instructor.email,
            phone=instructor.phone,
            department=instructor.department,
            created_at=instructor.created_at,
            updated_at=instructor.updated_at
        )
        return jsonify({"data": instructor_dto.to_dict()}), 200
    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500



@instructors_bp.route('/instructor/<int:id>', methods=['DELETE'])
def delete_instructor(id):
    try:
        instructor = Instructor.query.get(id)
        if not instructor:
            return jsonify({"message": "Instructor not found"}), 404
        db.session.delete(instructor)
        db.session.commit()
        return jsonify({"message": "Instructor deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
    

@instructors_bp.route('/instructor/<int:id>', methods=['PUT'])
def update_instructor(id):
    data = request.get_json()
    try:
        instructor = Instructor.query.get(id)
        if not instructor:
            return jsonify({"message": "Instructor not found"}), 404
        instructor.firstname = data.get('firstname', instructor.firstname)
        instructor.lastname = data.get('lastname', instructor.lastname)
        instructor.dob = datetime.strptime(data['dob'], '%Y-%m-%d') if 'dob' in data else instructor.dob
        instructor.gender = data.get('gender', instructor.gender)
        instructor.email = data.get('email', instructor.email)
        instructor.phone = data.get('phone', instructor.phone)
        instructor.department = data.get('department', instructor.department)
        instructor.updated_at = datetime.now() 
        instructor.created_at = datetime.now()
        db.session.commit()
        instructor_dto = InstructorDTO(
            id=instructor.id,
            firstname=instructor.firstname,
            lastname=instructor.lastname,
            dob=instructor.dob,
            gender=instructor.gender,
            email=instructor.email,
            phone=instructor.phone,
            department=instructor.department,
            created_at=instructor.created_at,
            updated_at=instructor.updated_at
        )
        return jsonify({"data": instructor_dto.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500




