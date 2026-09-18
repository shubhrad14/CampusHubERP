from app.models.enrollment import Enrollment


enrollments = []


def enroll_student(student, course):
    enrollment = Enrollment(student, course)

    enrollments.append(enrollment)

    print(
        f"Student {student.student_id} enrolled "
        f"in course {course.course_code} successfully."
    )

    return enrollment


def remove_enrollment(student_id, course_code):
    for enrollment in enrollments:

        if (
            enrollment.student.student_id == student_id
            and enrollment.course.course_code == course_code
        ):
            enrollments.remove(enrollment)

            print(
                f"Enrollment removed: "
                f"{student_id} - {course_code}"
            )

            return

    print(
        f"Enrollment not found for "
        f"{student_id} - {course_code}"
    )


def list_enrollments():

    print("\n----- ENROLLMENT LIST -----")

    if not enrollments:
        print("No enrollments available.")
        return

    for enrollment in enrollments:

        print(
            f"Student: {enrollment.student.student_id} | "
            f"Name: {enrollment.student.name} | "
            f"Course: {enrollment.course.course_code} | "
            f"Course Name: {enrollment.course.course_name}"
        )

