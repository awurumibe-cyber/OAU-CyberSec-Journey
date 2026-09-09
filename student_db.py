students = {}


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    students[student_id] = name

    print("Student added successfully.")


def search_student():
    student_id = input("Enter student ID to search: ")

    if student_id in students:
        print("Student:", students[student_id])
    else:
        print("Student not found.")


def delete_student():
    student_id = input("Enter student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


add_student()
search_student()
delete_student()

