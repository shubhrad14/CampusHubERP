from multiprocessing import Process, Queue


def calculate_statistics(
    students,
    faculty_members,
    courses,
    enrollments,
    result_queue
):
    total_students = len(students)
    total_faculty = len(faculty_members)
    total_courses = len(courses)
    total_enrollments = len(enrollments)

    result = {
        "Total Students": total_students,
        "Total Faculty": total_faculty,
        "Total Courses": total_courses,
        "Total Enrollments": total_enrollments
    }

    result_queue.put(result)


def run_statistics(
    students,
    faculty_members,
    courses,
    enrollments
):
    print("\n===== CALCULATING STATISTICS =====")

    result_queue = Queue()

    process = Process(
        target=calculate_statistics,
        args=(
            students,
            faculty_members,
            courses,
            enrollments,
            result_queue
        )
    )

    process.start()

    result = result_queue.get()

    process.join()

    print("\n----- OVERALL STATISTICS -----")

    print(f"Total Students: {result['Total Students']}")
    print(f"Total Faculty: {result['Total Faculty']}")
    print(f"Total Courses: {result['Total Courses']}")
    print(f"Total Enrollments: {result['Total Enrollments']}")

    return result

