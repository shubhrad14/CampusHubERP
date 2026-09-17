from app.utils.decorators import log_decorator, time_decorator
faculty_members = []

@log_decorator
@time_decorator
def add_faculty(faculty):
    faculty_members.append(faculty)
    print(f"Faculty {faculty.faculty_id} added successfully.")

@log_decorator
@time_decorator
def remove_faculty(faculty_id):
    for faculty in faculty_members:
        if faculty.faculty_id == faculty_id:
            faculty_members.remove(faculty)
            print(f"Faculty {faculty_id} removed successfully.")
            return

    print(f"Faculty {faculty_id} not found.")

@log_decorator
@time_decorator
def update_faculty(
    faculty_id,
    name=None,
    age=None,
    email=None,
    department=None
):
    for faculty in faculty_members:
        if faculty.faculty_id == faculty_id:

            if name is not None:
                faculty.name = name

            if age is not None:
                faculty.age = age

            if email is not None:
                faculty.email = email

            if department is not None:
                faculty.department = department

            faculty.update_timestamp()

            print(f"Faculty {faculty_id} updated successfully.")
            return

    print(f"Faculty {faculty_id} not found.")

@log_decorator
@time_decorator
def list_faculty():
    if not faculty_members:
        print("No faculty members available.")
        return

    print("\n----- Faculty List -----")

    for faculty in faculty_members:
        print(
            faculty.faculty_id,
            "|",
            faculty.name,
            "|",
            faculty.age,
            "|",
            faculty.email,
            "|",
            faculty.department
        )

def display_names_uppercase():
    names = map(lambda faculty: faculty.name.upper(), faculty_members)

    print("\n----- Faculty Names (Uppercase) -----")

    for name in names:
        print(name)


def filter_by_department(department):
    filtered_faculty = filter(
        lambda faculty: faculty.department.lower() == department.lower(),
        faculty_members
    )

    print(f"\n----- Faculty in {department} -----")

    found = False

    for faculty in filtered_faculty:
        found = True
        print(
            faculty.faculty_id,
            "|",
            faculty.name,
            "|",
            faculty.department
        )

    if not found:
        print("No faculty found in this department.")


def sort_faculty_by_name():
    sorted_faculty = sorted(
        faculty_members,
        key=lambda faculty: faculty.name.lower()
    )

    print("\n----- Faculty Sorted by Name -----")

    for faculty in sorted_faculty:
        print(
            faculty.faculty_id,
            "|",
            faculty.name,
            "|",
            faculty.department
        )

display_names_uppercase()

filter_by_department("Information Technology")

sort_faculty_by_name()