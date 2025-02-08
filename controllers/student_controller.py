from flask import request, jsonify
from models.students import db, Student
from datetime import datetime
import re

def is_valid_email(email):
    # Simple regex for validating an email
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

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
        
        return jsonify({
            'id': new_student.id,
            'firstname': new_student.firstname,
            'lastname': new_student.lastname,
            'dob': new_student.dob.strftime('%Y-%m-%d'),
            'gender': new_student.gender,
            'email': new_student.email,
            'phone': new_student.phone,
            'address': new_student.address
        }), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500