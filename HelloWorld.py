student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}
student2 = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

try:
    allStudents = [student["NEMLE"], student2]
    print(allStudents)
except KeyError as error:
    print("Error")
    print(error)


