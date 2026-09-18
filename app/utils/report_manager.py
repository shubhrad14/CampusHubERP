from app.utils.generators import (
    student_report,
    faculty_report,
    course_report
)

from app.utils.file_manager import ReportWriter


def generate_student_report(students):
    with ReportWriter("reports/student.txt") as report:

        report.write("====================================\n")
        report.write("         STUDENT REPORT\n")
        report.write("====================================\n\n")

        for student in student_report(students):
            report.write(
                f"Student ID: {student.student_id}\n"
            )
            report.write(
                f"Name: {student.name}\n"
            )
            report.write(
                f"Age: {student.age}\n"
            )
            report.write(
                f"Email: {student.email}\n"
            )
            report.write(
                f"Department: {student.department}\n"
            )
            report.write("------------------------------------\n")


def generate_faculty_report(faculty_members):
    with ReportWriter("reports/faculty.txt") as report:

        report.write("====================================\n")
        report.write("         FACULTY REPORT\n")
        report.write("====================================\n\n")

        for faculty in faculty_report(faculty_members):
            report.write(
                f"Faculty ID: {faculty.faculty_id}\n"
            )
            report.write(
                f"Name: {faculty.name}\n"
            )
            report.write(
                f"Age: {faculty.age}\n"
            )
            report.write(
                f"Email: {faculty.email}\n"
            )
            report.write(
                f"Department: {faculty.department}\n"
            )
            report.write("------------------------------------\n")


def generate_course_report(courses):
    with ReportWriter("reports/courses.txt") as report:

        report.write("====================================\n")
        report.write("         COURSE REPORT\n")
        report.write("====================================\n\n")

        for course in course_report(courses):
            report.write(
                f"Course Code: {course.course_code}\n"
            )
            report.write(
                f"Course Name: {course.course_name}\n"
            )
            report.write(
                f"Credits: {course.credits}\n"
            )
            report.write("------------------------------------\n")

