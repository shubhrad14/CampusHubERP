from app.core.abc_interfaces import Person
from app.core.descriptors import NonEmptyName, ValidEmail, ValidAge
from app.core.metaclasses import BaseModel


class Student(Person, BaseModel):

    name = NonEmptyName()
    email = ValidEmail()
    age = ValidAge()

    def __init__(self, student_id, name, age, email, department):
        BaseModel.__init__(self)

        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department

    def display_details(self):
        print("\n----- Student Details -----")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Email      :", self.email)
        print("Department :", self.department)
        print("Created At :", self.created_at)
        print("Updated At :", self.updated_at)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
if __name__ == "__main__":

    student = Student(
        "ST001",
        "Shubhra",
        21,
        "shubhra@gmail.com",
        "Information Technology"
    )

    student.display_details()

    print("\nDictionary:")
    print(student.to_dict())