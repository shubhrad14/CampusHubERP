def id_generator(prefix):
    count = 0

    def generate_id():
        nonlocal count
        count += 1
        return f"{prefix}{count:03d}"

    return generate_id

if __name__ == "__main__":

    student_id_generator = id_generator("ST")
    faculty_id_generator = id_generator("FC")
    course_id_generator = id_generator("CS")

    print("Student IDs:")
    print(student_id_generator())
    print(student_id_generator())
    print(student_id_generator())

    print("\nFaculty IDs:")
    print(faculty_id_generator())
    print(faculty_id_generator())

    print("\nCourse IDs:")
    print(course_id_generator())
    print(course_id_generator())