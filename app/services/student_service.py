from app.utils.decorators import log_decorator, time_decorator

students = []

@log_decorator
@time_decorator
def add_student(student):
    students.append(student)
    print(f"Student {student.student_id} added successfully.")

@log_decorator
@time_decorator
def remove_student(student_id):
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print(f"Student {student_id} removed successfully.")
            return

    print(f"Student {student_id} not found.")

@log_decorator
@time_decorator
def update_student(student_id, name=None, age=None, email=None, department=None):
    for student in students:
        if student.student_id == student_id:

            if name is not None:
                student.name = name

            if age is not None:
                student.age = age

            if email is not None:
                student.email = email

            if department is not None:
                student.department = department

            student.update_timestamp()

            print(f"Student {student_id} updated successfully.")
            return

    print(f"Student {student_id} not found.")

@log_decorator
@time_decorator
def list_students():
    if not students:
        print("No students available.")
        return

    print("\n----- Student List -----")

    for student in students:
        print(
            student.student_id,
            "|",
            student.name,
            "|",
            student.age,
            "|",
            student.email,
            "|",
            student.department
        )

def display_names_uppercase():
    names = map(lambda student: student.name.upper(), students)

    print("\n----- Student Names (Uppercase) -----")

    for name in names:
        print(name)


def filter_by_department(department):
    filtered_students = filter(
        lambda student: student.department.lower() == department.lower(),
        students
    )

    print(f"\n----- Students in {department} -----")

    found = False

    for student in filtered_students:
        found = True
        print(
            student.student_id,
            "|",
            student.name,
            "|",
            student.department
        )

    if not found:
        print("No students found in this department.")


def sort_students_by_name():
    sorted_students = sorted(
        students,
        key=lambda student: student.name.lower()
    )

    print("\n----- Students Sorted by Name -----")

    for student in sorted_students:
        print(
            student.student_id,
            "|",
            student.name,
            "|",
            student.department
        )

if __name__ == "__main__":
    display_names_uppercase()
    filter_by_department("Information Technology")
    sort_students_by_name()

