from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


def main():

    print("======================================")
    print("        CAMPUSHUB ERP SYSTEM")
    print("======================================")

    # Creating Student objects
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

    # Creating Faculty object
    faculty1 = Faculty(
        "FC001",
        "Dr. Mehta",
        45,
        "mehta@college.edu",
        "Information Technology"
    )

    # Creating Course objects
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

    # Display Student details
    student1.display_details()
    student2.display_details()

    # Display Faculty details
    faculty1.display_details()

    # Display Course details
    course1.display_details()
    course2.display_details()


if __name__ == "__main__":
    main()