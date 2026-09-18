
import threading

from app.utils.report_manager import (
    generate_student_report,
    generate_faculty_report,
    generate_course_report
)

def generate_reports_concurrently(
    students,
    faculty_members,
    courses
):
    print("\n===== REPORT GENERATION STARTED =====")

    print("Generating Student Report...")
    print("Generating Faculty Report...")
    print("Generating Course Report...")

    student_thread = threading.Thread(
        target=generate_student_report,
        args=(students,)
    )

    faculty_thread = threading.Thread(
        target=generate_faculty_report,
        args=(faculty_members,)
    )

    course_thread = threading.Thread(
        target=generate_course_report,
        args=(courses,)
    )

    student_thread.start()
    faculty_thread.start()
    course_thread.start()

    student_thread.join()
    faculty_thread.join()
    course_thread.join()

    print("Done.")
    print("All reports generated successfully.")

