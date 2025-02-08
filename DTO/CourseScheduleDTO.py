from datetime import datetime
import pytz

CAMBODIA_TZ = pytz.timezone('Asia/Phnom_Penh')

class CourseScheduleDTO:
    def __init__(self, id, day_of_week, start_time, end_time, room_number, created_at, updated_at, course_name=None, instructor_name=None):
        self.id = id
        self.day_of_week = day_of_week
        self.start_time = self.convert_to_cambodia_time(start_time)
        self.end_time = self.convert_to_cambodia_time(end_time)
        self.room_number = room_number
        self.created_at = self.convert_to_cambodia_time(created_at)
        self.updated_at = self.convert_to_cambodia_time(updated_at)
        self.course_name = course_name
        self.instructor_name = instructor_name

    def convert_to_cambodia_time(self, dt):
        if dt is None:
            return None
        return dt.astimezone(CAMBODIA_TZ) if dt.tzinfo else CAMBODIA_TZ.localize(dt)
    def to_dict(self):
        return {
            "id": self.id,
            "day_of_week": self.day_of_week,
            "start_time": self.start_time.strftime('%Y-%m-%d %H:%M:%S') if self.start_time else None,
            "end_time": self.end_time.strftime('%Y-%m-%d %H:%M:%S') if self.end_time else None,
            "room_number": self.room_number,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None,
            "course_name": self.course_name,
            "instructor_name": self.instructor_name
        }
