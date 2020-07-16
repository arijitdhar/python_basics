__author__ = '220152'

"""
import datetime
current_date_time = datetime.datetime.now()
print("The date and time is", current_date_time)


x = 10
y = '10'
z = 10.1

sum = x + z

print(type(x), type(y), type(z))
print(type(sum))
"""


student_grades_list = [9.1, 8.8, 7.5, 9.1]


grade_sum = sum(student_grades_list)
max_grade = max(student_grades_list)
min_grade = min(student_grades_list)
number_of_grades = len(student_grades_list)
average_grade = grade_sum/number_of_grades



print("grade_sum", grade_sum)
print("average_grade", average_grade)
print("max grade", max_grade)
print("min grade", min_grade)

print("max grade count", student_grades_list.count(max_grade))

student_grades_dict = {"A": 9.1, "B": 8.8, "C": 7.5, "D":9.1}
student_grade_sum = sum(student_grades_dict.values())
student_max_grade = max(student_grades_dict.values())
student_min_grade = min(student_grades_dict.values())
student_number_of_grades = len(student_grades_dict)
student_average_grade = student_grade_sum/student_number_of_grades


print("student_grade_sum", student_grade_sum)
print("student_average_grade", student_average_grade)
print("student_max_grade", student_max_grade)
print("student_min_grade", student_min_grade)

#print(type(student_grades))

#num_range = list(range(1,10,2))
#print(num_range)

"""
List can contain heterogeneous data types as well as nested lists
"""
#temperature_list = [ 20.5, 18, "City 1"]

#print(temperature_list)

#print("hello".title()) #capitalizes the first letter
#print(dir(str)) # prints the attributes/methods for a type

#print("hello".isalpha())

#get a list of built in functions we can use in python
#print(dir(__builtins__))


# to get help on a function use help()
# help(str.upper)

# to get information about built in modules, use
# import sys
# sys.builtin_module_names

# to check the info about non built in modules like os
# import sys
# sys.prefix # gives the location of the python installation directory ('C:\\Python36', in my case)

########################### tuples ######################## A list with parentheses instead of square bracket in list
# tuples are immutable, we can use append() and remove() in lists.
# tuples are faster than list

monday_temperatures = (10, 12.0, 11)
print("monday temperatures", monday_temperatures)


####### List slice ########### the end limit is not included
# during list slicing, always remember, start position is inclusive and end position is exclusive
list_1 = [10.0, 11.0, 12.0]
print(list_1[0:2]) # get the first 2 items

print(list_1[2:]) # get the last items starting from the 3rd item

print(list_1[-1]) # get the last item, since -ve index start from last, and positive index start as 0 from beginning


print(list_1[-3:]) # get the last 3 items
print(list_1[:3]) # get the first 3 items