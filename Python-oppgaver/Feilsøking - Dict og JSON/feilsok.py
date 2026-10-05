# import json
#
# def read_students(filename):
#     with open(filename, "r") as f:
#         data = json.load(f)
#     return data
#
# def average_grade(grades):
#     total = 0
#     for g in grades:
#         total = total + g
#     return total / len(grades)
#
# def show_student(student):
#     name = student["navn"]
#     age = student["alder"]
#     city = student["by"]
#     avg = average_grade(student["karakterer"])
#
#     print(f"Navn: {name}, alder: {age}, by: {city}")
#     print("Snittkarakter: ", avg)
#
# def main():
#     data = read_students("studenter.json")
#     students = data["studenter"]
#
#     for student in students:
#         show_student(student)
#
#         if student["alder"] <= 21:
#             print(student["navn"] + " er den yngste vi har registrert")
#
#     print("Antall studenter:", len(students))
#
# main()

