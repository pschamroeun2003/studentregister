from flask import Blueprint, request, jsonify
from models.courses import Course
from extensions import db
from datetime import datetime
from DTO.CourseDTO import CourseDTO

from flask import Blueprint, request, jsonify
from datetime import datetime
from models.enrollments import Enrollment
from models.students import Student
from models.courses import Course  # Import the Course model
from extensions import db
from DTO.EnrollmentDTO import EnrollmentDTO
from ENUM.enrollment_status import EnrollmentStatus

enrollment_bp = Blueprint('enrollment', __name__, url_prefix='/api/enrollments')

@enrollment_bp.route('/enrollment', methods=['POST'])
def enroll_student():
    data = request.get_json()
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    status = data.get('status').upper()
    if status not in [e.name for e in EnrollmentStatus]:
        return jsonify({'message': f'Invalid status: {status}'}), 400
    status_enum = EnrollmentStatus[status]
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'message': 'Course not found'}), 404
    enrollment = Enrollment(
        student_id=student_id,
        course_id=course_id,
        status=status_enum
    )
    db.session.add(enrollment)
    db.session.commit()
    enrollment_dto = EnrollmentDTO(
        id=enrollment.id,
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        status=enrollment.status,
        firstname=student.firstname,
        lastname=student.lastname,
        created_at=enrollment.created_at,
        updated_at=enrollment.updated_at
    )
    return jsonify({
        'message': 'Enrollment created successfully',
        'enrollment': enrollment_dto.to_dict()
    }), 201

@enrollment_bp.route('/enrollment', methods=['GET'])
def get_all_enrollments():
    enrollments = Enrollment.query.all()
    enrollment_list = []
    for enrollment in enrollments:
        student = Student.query.get(enrollment.student_id)
        enrollment_dto = EnrollmentDTO(
            id=enrollment.id,
            student_id=enrollment.student_id,
            course_id=enrollment.course_id,
            status=enrollment.status,
            firstname=student.firstname,
            lastname=student.lastname,
            created_at=enrollment.created_at,
            updated_at=enrollment.updated_at
        )
        enrollment_list.append(enrollment_dto.to_dict())
    return jsonify({'data': enrollment_list})

@enrollment_bp.route('/enrollment/<int:id>', methods=['GET'])
def get_enrollment(id):
    enrollment = Enrollment.query.get(id)
    if not enrollment:
        return jsonify({'message': 'Enrollment not found'}), 404
    student = Student.query.get(enrollment.student_id)
    enrollment_dto = EnrollmentDTO(
        id=enrollment.id,
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        status=enrollment.status,
        firstname=student.firstname,
        lastname=student.lastname,
        created_at=enrollment.created_at,
        updated_at=enrollment.updated_at
    )
    return jsonify({'data': enrollment_dto.to_dict()})

@enrollment_bp.route('/enrollment/<int:id>', methods=['PUT'])
def update_enrollment(id):
    data = request.get_json()
    status = data.get('status').upper()
    
    if status not in [e.name for e in EnrollmentStatus]:
        return jsonify({'message': f'Invalid status: {status}'}), 400
    status_enum = EnrollmentStatus[status]

    enrollment = Enrollment.query.get(id)
    if not enrollment:
        return jsonify({'message': 'Enrollment not found'}), 404

    enrollment.status = status_enum
    db.session.commit()

    student = Student.query.get(enrollment.student_id)
    enrollment_dto = EnrollmentDTO(
        id=enrollment.id,
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        status=enrollment.status,
        firstname=student.firstname,
        lastname=student.lastname,
        created_at=enrollment.created_at,
        updated_at=enrollment.updated_at
    )
    
    return jsonify({
        'message': 'Enrollment updated successfully',
        'data': enrollment_dto.to_dict()
    })
@enrollment_bp.route('/enrollment/<int:id>', methods=['DELETE'])
def delete_enrollment(id):
    enrollment = Enrollment.query.get(id)
    if not enrollment:
        return jsonify({'message': 'Enrollment not found'}), 404

    db.session.delete(enrollment)
    db.session.commit()

    return jsonify({'message': 'Enrollment deleted successfully'})

