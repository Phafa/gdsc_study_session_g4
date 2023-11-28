def add_student():
    student_name = input("Enter student name: ")
    student_age = int(input("Enter student age: "))
    student_grade = int(input("Enter student grade: "))

    student_data = {
        "name": student_name,
        "age": student_age,
        "grade": student_grade
    }

    students.append(student_data)
    print("Student added successfully!")

def view_student():
    student_name = input("Enter student name to view: ")

    for student in students:
        if student["name"] == student_name:
            print("Student Details:")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Grade:", student["grade"])
            return

    print("Student not found in the database.")

def list_all_students():
    if not students:
        print("No students in the database.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        print("-----------------------")

def update_student():
    student_name = input("Enter student name to update: ")

    for i, student in enumerate(students):
        if student["name"] == student_name:
            new_age = int(input("Enter new student age: "))
            new_grade = int(input("Enter new student grade: "))

            students[i]["age"] = new_age
            students[i]["grade"] = new_grade