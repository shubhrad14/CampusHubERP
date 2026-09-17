from app.utils.decorators import log_decorator, time_decorator

courses = []

@log_decorator
@time_decorator
def add_course(course):
    courses.append(course)
    print(f"Course {course.course_code} added successfully.")

@log_decorator
@time_decorator
def remove_course(course_code):
    for course in courses:
        if course.course_code == course_code:
            courses.remove(course)
            print(f"Course {course_code} removed successfully.")
            return

    print(f"Course {course_code} not found.")

@log_decorator
@time_decorator
def update_course(
    course_code,
    course_name=None,
    credits=None
):
    for course in courses:
        if course.course_code == course_code:

            if course_name is not None:
                course.course_name = course_name

            if credits is not None:
                course.credits = credits

            course.update_timestamp()

            print(f"Course {course_code} updated successfully.")
            return

    print(f"Course {course_code} not found.")

@log_decorator
@time_decorator
def list_courses():
    if not courses:
        print("No courses available.")
        return

    print("\n----- Course List -----")

    for course in courses:
        print(
            course.course_code,
            "|",
            course.course_name,
            "| Credits:",
            course.credits
        )

def display_course_names_uppercase():
    names = map(lambda course: course.course_name.upper(), courses)

    print("\n----- Course Names (Uppercase) -----")

    for name in names:
        print(name)


def sort_courses_by_name():
    sorted_courses = sorted(
        courses,
        key=lambda course: course.course_name.lower()
    )

    print("\n----- Courses Sorted by Name -----")

    for course in sorted_courses:
        print(
            course.course_code,
            "|",
            course.course_name,
            "| Credits:",
            course.credits
        )

display_course_names_uppercase()

sort_courses_by_name()