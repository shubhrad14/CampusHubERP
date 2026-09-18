class Enrollment:

    def __init__(self, student, course):
        self.student = student
        self.course = course

    def display_details(self):
        print(
            f"Student: {self.student.student_id} | "
            f"Course: {self.course.course_code}"
        )

    def to_dict(self):
        return {
            "student_id": self.student.student_id,
            "course_code": self.course.course_code
        }