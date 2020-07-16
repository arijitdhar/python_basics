# __author__ = '220152'
#
# monday_temperatures = [10.5, 11.4, 12.1]
# name = "Arijit"
# for temp in monday_temperatures:
#     print(round(temp))
#
# for letter in name:
#     print(letter.title())
#
# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
# for color in colors:
#     if isinstance(color, int):
#         print(color)

# student_grades = {"A": 10, "B": 11}
#
# for grades in student_grades.items(): # this gives tuples
#     print(grades)
#
#
# for grades in student_grades.keys():
#     print(grades)
#
# for grades in student_grades.values():
#     print(grades)
#
# for grades in student_grades.items():
#     message = f"Key: {grades[0]}, Value: {grades[1]}"
#     print(message)
#
# for key, value in student_grades.items():
#     print("Key: {}, Value: {}".format(key, value))
#
# phone_numbers = {"John_Smith": "+398239812", "Mary Simpons": "+313132213"}
# for key, value in phone_numbers.items():
#     print(value.replace('+', '00'))


username = ""

# while username != "pypy":
#     username = input("Enter username: ")

while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue




