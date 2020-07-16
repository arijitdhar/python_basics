__author__ = '220152'

user_name = input("Enter your name:")
user_age = input("Enter your age:")

# Formatting Strings using old school % style formatting
message = "Hello %s, your age is %s" % (user_name, user_age)

# Formatting string using python 2.6 String.format()
message = "Hello {}, your age {}".format(user_name, user_age)

# Formatting string using python 3.6 f-strings
message = f"Hello {user_name}, your age: {user_age}"
print(message)


def greeting(name):
    message =  "Hi %s" % name.title()
    return message

print(greeting(user_name))


