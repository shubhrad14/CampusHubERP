from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course

from app.services.enrollment_service import (
    enroll_student,
    list_enrollments
)

from app.services.threading_service import (
    generate_reports_concurrently
)

from app.services.multiprocessing_service import (
    run_statistics
)

from app.services.student_service import (
    add_student,
    update_student,
    remove_student,
    list_students,
    display_names_uppercase,
    filter_by_department,
    sort_students_by_name
)

from app.services.faculty_service import (
    add_faculty,
    update_faculty,
    remove_faculty,
    list_faculty,
    display_names_uppercase as display_faculty_names_uppercase,
    filter_by_department as filter_faculty_by_department,
    sort_faculty_by_name
)

from app.services.course_service import (
    add_course,
    update_course,
    remove_course,
    list_courses,
    display_course_names_uppercase,
    sort_courses_by_name
)


def main():

    print("======================================")
    print("       CAMPUSHUB ERP - WEEK 2")
    print("======================================")

    # ---------------- STUDENTS ----------------

    student1 = Student(
        "ST001",
        "Shubhra",
        21,
        "shubhra@gmail.com",
        "Information Technology"
    )

    student2 = Student(
        "ST002",
        "Rahul",
        22,
        "rahul@gmail.com",
        "Computer Science"
    )

    add_student(student1)
    add_student(student2)

    list_students()

    display_names_uppercase()

    filter_by_department("Information Technology")

    sort_students_by_name()

    # ---------------- FACULTY ----------------

    faculty1 = Faculty(
        "FC001",
        "Dr. Mehta",
        45,
        "mehta@college.edu",
        "Information Technology"
    )

    faculty2 = Faculty(
        "FC002",
        "Dr. Sharma",
        42,
        "sharma@college.edu",
        "Computer Science"
    )

    add_faculty(faculty1)
    add_faculty(faculty2)

    list_faculty()

    display_faculty_names_uppercase()

    filter_faculty_by_department("Information Technology")

    sort_faculty_by_name()

    # ---------------- COURSES ----------------

    course1 = Course(
        "CS101",
        "Python Programming",
        4
    )

    course2 = Course(
        "CS102",
        "Database Management",
        3
    )

    add_course(course1)
    add_course(course2)

    list_courses()

    display_course_names_uppercase()

    sort_courses_by_name()

        # ---------------- ENROLLMENTS ----------------

    enrollment1 = enroll_student(student1, course1)
    enrollment2 = enroll_student(student2, course2)

    list_enrollments()

    # ---------------- THREADING ----------------

    generate_reports_concurrently(
        [student1, student2],
        [faculty1, faculty2],
        [course1, course2]
    )

    # ---------------- MULTIPROCESSING ----------------

    run_statistics(
        [student1, student2],
        [faculty1, faculty2],
        [course1, course2],
        [enrollment1, enrollment2]
    )


if __name__ == "__main__":
    main()