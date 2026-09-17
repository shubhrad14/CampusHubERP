from app.core.abc_interfaces import Person
from app.core.descriptors import NonEmptyName, ValidEmail, ValidAge
from app.core.metaclasses import BaseModel


class Faculty(Person, BaseModel):

    name = NonEmptyName()
    email = ValidEmail()
    age = ValidAge()

    def __init__(self, faculty_id, name, age, email, department):
        BaseModel.__init__(self)

        self.faculty_id = faculty_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department

    def display_details(self):
        print("\n----- Faculty Details -----")
        print("Faculty ID :", self.faculty_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Email      :", self.email)
        print("Department :", self.department)
        print("Created At :", self.created_at)
        print("Updated At :", self.updated_at)

    def to_dict(self):
        return {
            "faculty_id": self.faculty_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


if __name__ == "__main__":
    faculty = Faculty(
        "FC001",
        "Dr. Mehta",
        45,
        "mehta@college.edu",
        "Information Technology"
    )

    faculty.display_details()

    print("\nDictionary:")
    print(faculty.to_dict())