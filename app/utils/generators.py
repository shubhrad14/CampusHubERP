def id_generator(prefix):
    count = 0

    def generate_id():
        nonlocal count
        count += 1
        return f"{prefix}{count:03d}"

    return generate_id

def student_report(students):
    for student in students:
        yield student


def faculty_report(faculty_members):
    for faculty in faculty_members:
        yield faculty


def course_report(courses):
    for course in courses:
        yield course

