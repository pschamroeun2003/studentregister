from flask import Blueprint, request, jsonify
from models.grades import Grade
from extensions import db
from DTO.GradeDTO import GradeDTO
from datetime import datetime
grade_bp = Blueprint('grade', __name__, url_prefix='/api/grades')
@grade_bp.route('/grade', methods=['POST'])
def add_grade():
    data = request.get_json()
    required_fields = ['student_id', 'course_id', 'grade', 'semester']
    if not data or not all(key in data for key in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    try:
        new_grade = Grade(
            student_id=data['student_id'],
            course_id=data['course_id'],
            grade=data['grade'],
            semester=data['semester'],
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(new_grade)
        db.session.commit()
        grade_dto = GradeDTO(
            id=new_grade.id,
            student_id=new_grade.student_id,
            course_id=new_grade.course_id,
            course_name=new_grade.course.course_name,
            student_firstname=new_grade.student.firstname,
            student_lastname=new_grade.student.lastname,
            grade=new_grade.grade,
            semester=new_grade.semester,
            created_at=new_grade.created_at,
            updated_at=new_grade.updated_at
        )
        return jsonify(grade_dto.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500



@grade_bp.route('/grade', methods=['GET'])
def get_all_grades():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        grades = Grade.query.paginate(page=page, per_page=per_page, error_out=False)
        grade_dtos = [GradeDTO(
            id=grade.id,
            student_id=grade.student_id,
            course_id=grade.course_id,
            course_name=grade.course.course_name,
            student_firstname=grade.student.firstname,
            student_lastname=grade.student.lastname,
            grade=grade.grade,
            semester=grade.semester,
            created_at=grade.created_at,
            updated_at=grade.updated_at
        ) for grade in grades.items]
        pagination = {
            "page": grades.page,
            "per_page": grades.per_page,
            "total": grades.total,
            "pages": grades.pages
        }
        next_page_link = f"/api/grades/grade?page={grades.page + 1}&per_page={grades.per_page}" if grades.has_next else None
        prev_page_link = f"/api/grades/grade?page={grades.page - 1}&per_page={grades.per_page}" if grades.has_prev else None
        return jsonify({
            "pagination": pagination,
            "grades": [grade.to_dict() for grade in grade_dtos],
            "next_page_link": next_page_link,
            "prev_page_link": prev_page_link,
        }), 200
    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500

@grade_bp.route('/grade/<int:id>', methods=['GET'])
def get_grade(id):
    try:
        grade = Grade.query.get(id)
        if not grade:
            return jsonify({"message": "Grade not found"}), 404
        grade_dto = GradeDTO(
            id=grade.id,
            student_id=grade.student_id,
            course_id=grade.course_id,
            course_name=grade.course.course_name,
            student_firstname=grade.student.firstname,
            student_lastname=grade.student.lastname,
            grade=grade.grade,
            semester=grade.semester,
            created_at=grade.created_at,
            updated_at=grade.updated_at
        )
        return jsonify(grade_dto.to_dict()), 200
    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500


@grade_bp.route('/grade/<int:id>', methods=['PUT'])
def update_grade(id):
    data = request.get_json()
    try:
        grade = Grade.query.get(id)
        if not grade:
            return jsonify({"message": "Grade not found"}), 404
        grade.grade = data.get('grade', grade.grade)
        grade.semester = data.get('semester', grade.semester)
        grade.updated_at = datetime.now()
        db.session.commit()
        grade_dto = GradeDTO(
            id=grade.id,
            student_id=grade.student_id,
            course_id=grade.course_id,
            course_name=grade.course.course_name,
            student_firstname=grade.student.firstname,
            student_lastname=grade.student.lastname,
            grade=grade.grade,
            semester=grade.semester,
            created_at=grade.created_at,
            updated_at=grade.updated_at
        )
        return jsonify(grade_dto.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500

@grade_bp.route('/grade/<int:id>', methods=['DELETE'])
def delete_grade(id):
    try:
        grade = Grade.query.get(id)
        if not grade:
            return jsonify({"message": "Grade not found"}), 404
        db.session.delete(grade)
        db.session.commit()
        return jsonify({"message": "Grade deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
