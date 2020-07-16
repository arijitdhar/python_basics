__author__ = '220152'

import logging

LOGGER = logging.getLogger()

formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs).03d] [%(name)s,%(funcName)s:%(lineno)s] [%(levelname)s]  %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

LOGGER.addHandler(console_handler)
LOGGER.setLevel(logging.INFO)


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    elif type(value) == list:
        the_mean = sum(value)/len(value)
    else:
        the_mean = "No mean"
    return the_mean


def mean_v2(value):
    if isinstance(value, dict):
        the_mean = sum(value.values())/len(value)
    elif isinstance(value, list):
        the_mean = sum(value)/len(value)
    else:
        the_mean = "No mean"
    return the_mean

student_grades = {"A": 10, "B": 11}
monday_temperatures = [10, 11]
print(mean(monday_temperatures))
print(mean_v2(monday_temperatures))


# positional and keyword arguments

def calculate_area(a, b):
    return a * b
# keyword argument, order does not matter
print(calculate_area(b=4, a=2))
# positional argument, order of arguments matter
print(calculate_area(2, 4))


# default parameters, always to be placed after non-default parameters
def calculate_volume(a, b=5, c=6):
    return a * b * c

print("test volume", calculate_volume(2, 6))
print(calculate_volume(2, 3, 8))


# Arbitrary number of non-default parameters
# *args is a tuple
def mean(*args):
    print(type(args))
    return sum(args)/len(args)

print("Mean: ", mean(1, 2, 3, 4))


# Arbitrary number of keyword arguments
# kwargs is a dict
def mean(**kwargs):
    print(type(kwargs))
    LOGGER.info("Keyword Arguments")
    return sum(kwargs.values())/len(kwargs)

print("Mean: ", mean(a=1, b=2, c=3, d=4))