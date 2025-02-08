from flask import Blueprint, request, jsonify
from models.curseschedules import CourseSchedule
from extensions import db
from datetime import datetime
from DTO.CourseScheduleDTO import CourseScheduleDTO

courseschedules_bp = Blueprint('courseschedules', __name__, url_prefix='/api/courseschedules')

@courseschedules_bp.route('/courseschedule', methods=['POST'])
def add_course_schedule():
    data = request.get_json()
    required_fields = ['course_id', 'instructor_id', 'day_of_week', 'start_time', 'end_time', 'room_number']
    
    if not data or not all(key in data for key in required_fields):
        return jsonify({"message": "Missing required fields"}), 400
    
    try:
        new_schedule = CourseSchedule(
            course_id=data['course_id'],
            instructor_id=data['instructor_id'],
            day_of_week=data['day_of_week'],
            start_time=datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S'),
            end_time=datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S'),
            room_number=data['room_number'],
            created_at=datetime.utcnow()
        )
        db.session.add(new_schedule)
        db.session.commit()
        schedule_dto = CourseScheduleDTO(
            id=new_schedule.id,
            day_of_week=new_schedule.day_of_week,
            start_time=new_schedule.start_time,
            end_time=new_schedule.end_time,
            room_number=new_schedule.room_number,
            created_at=new_schedule.created_at,
            updated_at=new_schedule.updated_at,
            course_name=new_schedule.course.course_name if new_schedule.course else None,
            instructor_name=f"{new_schedule.instructor.firstname} {new_schedule.instructor.lastname}" if new_schedule.instructor else None
        )
        return jsonify({"data": schedule_dto.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500


@courseschedules_bp.route('/courseschedule', methods=['GET'])
def get_course_schedules():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        schedules = CourseSchedule.query.paginate(page=page, per_page=per_page, error_out=False)
        schedule_dtos = [CourseScheduleDTO(
            id=course_schedule.id,
            day_of_week=course_schedule.day_of_week,
            start_time=course_schedule.start_time,
            end_time=course_schedule.end_time,
            room_number=course_schedule.room_number,
            created_at=course_schedule.created_at,
            updated_at=course_schedule.updated_at,
            course_name=course_schedule.course.course_name if course_schedule.course else None,
            instructor_name=f"{course_schedule.instructor.firstname} {course_schedule.instructor.lastname}" if course_schedule.instructor else None
        ) for course_schedule in schedules.items]
        pagination = {
            "page": schedules.page,
            "per_page": schedules.per_page,
            "total": schedules.total,
            "pages": schedules.pages
        }

        next_page_link = f"/api/courseschedules/courseschedule?page={schedules.page + 1}&per_page={schedules.per_page}" if schedules.has_next else None
        prev_page_link = f"/api/courseschedules/courseschedule?page={schedules.page - 1}&per_page={schedules.per_page}" if schedules.has_prev else None

        return jsonify({
            "pagination": pagination,
            "courseschedules": [schedule.to_dict() for schedule in schedule_dtos],
            "next_page_link": next_page_link,
            "prev_page_link": prev_page_link
        }), 200
    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
    

@courseschedules_bp.route('/courseschedule/<int:id>', methods=['GET'])
def get_course_schedule(id):
    try:
        course_schedule = CourseSchedule.query.get(id)
        if not course_schedule:
            return jsonify({"message": "Course schedule not found"}), 404

        schedule_dto = CourseScheduleDTO(
            id=course_schedule.id,
            day_of_week=course_schedule.day_of_week,
            start_time=course_schedule.start_time,
            end_time=course_schedule.end_time,
            room_number=course_schedule.room_number,
            created_at=course_schedule.created_at,
            updated_at=course_schedule.updated_at,
            course_name=course_schedule.course.course_name if course_schedule.course else None,
            instructor_name=f"{course_schedule.instructor.firstname} {course_schedule.instructor.lastname}" if course_schedule.instructor else None
        )
        return jsonify({"data": schedule_dto.to_dict()}), 200
    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
    


@courseschedules_bp.route('/courseschedule/<int:id>', methods=['PUT'])
def update_course_schedule(id):
    data = request.get_json()
    try:
        course_schedule = CourseSchedule.query.get(id)
        if not course_schedule:
            return jsonify({"message": "Course schedule not found"}), 404
        course_schedule.day_of_week = data.get('day_of_week', course_schedule.day_of_week)
        course_schedule.start_time = datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S') if 'start_time' in data else course_schedule.start_time
        course_schedule.end_time = datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S') if 'end_time' in data else course_schedule.end_time
        course_schedule.room_number = data.get('room_number', course_schedule.room_number)
        course_schedule.updated_at = datetime.utcnow()
        db.session.commit()
        schedule_dto = CourseScheduleDTO(
            id=course_schedule.id,
            day_of_week=course_schedule.day_of_week,
            start_time=course_schedule.start_time,
            end_time=course_schedule.end_time,
            room_number=course_schedule.room_number,
            created_at=course_schedule.created_at,
            updated_at=course_schedule.updated_at,
            course_name=course_schedule.course.course_name if course_schedule.course else None,
            instructor_name=f"{course_schedule.instructor.firstname} {course_schedule.instructor.lastname}" if course_schedule.instructor else None
        )
        return jsonify({"data": schedule_dto.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500
    

@courseschedules_bp.route('/courseschedule/<int:id>', methods=['DELETE'])
def delete_course_schedule(id):
    try:
        course_schedule = CourseSchedule.query.get(id)
        if not course_schedule:
            return jsonify({"message": "Course schedule not found"}), 404
        db.session.delete(course_schedule)
        db.session.commit()
        return jsonify({"message": "Course schedule deleted successfully" , "status":"success"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500



