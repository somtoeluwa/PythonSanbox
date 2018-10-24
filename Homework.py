students = []


def add_student(name="John Snow", student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def print_all_students():
    print(students)


answer = input("Do you want to add a new student (Yes/No): ")


while answer.lower() == "yes":
    try:
        add_student(input("Enter Student name: "), input("Enter Student id: "))
        answer = input("Do you want to add another student (Yes/No): ")
    except TypeError as error:
        print(f"Error in Input {error}")
if answer.lower() == "no":
    print_all_students()
