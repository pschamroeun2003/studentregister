from flask import Blueprint, request, jsonify
from models.courses import Course
from extensions import db
from datetime import datetime
from DTO.CourseDTO import CourseDTO
course_bp = Blueprint('course', __name__, url_prefix='/api/courses')

@course_bp.route('/course', methods=['POST'])
def add_course():
    data = request.get_json()
    required_fields = ['course_name', 'code', 'credits', 'department']
    if not data or not all(key in data for key in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    
    try:
        new_course = Course(
            course_name=data['course_name'],
            code=data['code'],
            credits=data['credits'],
            department=data['department'],
        )
        db.session.add(new_course)
        db.session.commit()
        course_dto = CourseDTO(
            id=new_course.id,
            course_name=new_course.course_name,
            code=new_course.code,
            credits=new_course.credits,
            department=new_course.department,
            created_at=new_course.created_at
        )
        return jsonify(course_dto.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500

@course_bp.route('/course', methods=['GET'])
def get_all_course():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        if per_page < 1 or per_page > 100:
            return jsonify({"message": "'per_page' must be between 1 and 100"}), 400
        courses = Course.query.paginate(page=page, per_page=per_page, error_out=False)
        course_dtos = [CourseDTO(
            id=course.id,
            course_name=course.course_name,
            code=course.code,
            credits=course.credits,
            department=course.department,
            created_at=course.created_at,
            updated_at=course.updated_at
        ).to_dict() for course in courses.items]
        pagination = {
            "page": courses.page,
            "per_page": courses.per_page,
            "total_items": courses.total,
            "total_pages": courses.pages,
        }
        next_page_link = f"/api/courses/course?page={courses.page + 1}&per_page={courses.per_page}" if courses.has_next else None
        prev_page_link = f"/api/courses/course?page={courses.page - 1}&per_page={courses.per_page}" if courses.has_prev else None
        return jsonify({
            "pagination": pagination,
            "courses": course_dtos,
            "next_page_link": next_page_link,
            "prev_page_link": prev_page_link,
        }), 200

    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500


@course_bp.route('/<int:id>', methods=['GET'])
def get_course(id):
    try:
        course = Course.query.get_or_404(id)
        course_dto = CourseDTO(
            id=course.id,
            course_name=course.course_name,
            code=course.code,
            credits=course.credits,
            department=course.department,
            created_at=course.created_at
        )
        return jsonify(course_dto.to_dict()), 200
    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500


@course_bp.route('/<int:id>', methods=['PUT'])
def update_course(id):
    data = request.get_json()
    required_fields = ['course_name', 'code', 'credits', 'department']
    if not data or not all(key in data for key in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    try:
        course = Course.query.get_or_404(id)
        course.course_name = data['course_name']
        course.code = data['code']
        course.credits = data['credits']
        course.department = data['department']
        db.session.commit()

        course_dto = CourseDTO(
            id=course.id,
            course_name=course.course_name,
            code=course.code,
            credits=course.credits,
            department=course.department,
            created_at=course.created_at
        )

        return jsonify(course_dto.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500

@course_bp.route('/<int:id>', methods=['DELETE'])
def delete_course(id):
    try:
        course = Course.query.get_or_404(id)
        db.session.delete(course)
        db.session.commit()
        return jsonify({"message": "Course deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
