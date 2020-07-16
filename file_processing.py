__author__ = '220152'

#my_file = open('files/fruits.txt')
#print(type(my_file))
#content = my_file.read()# file.read() places the cursor at the end, so issuing the read() multiple times, will not help
#my_file.close() # to free the memory
#cannot open a file on a closed file
#print(content)

#file operation using with context manager, no need to explicitly close()
# with open('fruits.txt') as myfile:
#     content = myfile.read()
#
# print(content)

# with open('files/fruits.txt') as myfile:
#      content = myfile.read()
#
# print(content)


#Write to a file
# with open("files/fruits.txt") as input_file:
#     content = input_file.read()
#     first_90_characters = content[:9]
#
# with open("files/first.txt", "w") as output_file:
#     output_file.write(first_90_characters)

# #Appending to a file
# with open("files/fruits.txt", "a") as my_file:
#     my_file.write("\nGuava")
#     # my_file.read() # error as file is not open in read mode

#To read and append to a file use mode= a+
# with open("files/fruits.txt", "a+") as my_file:
#     my_file.write("\nGuava")
#     # without seek(0) we will get empty content here, since cursor was already at the end of the file when opened with "a+" mode
#     my_file.seek(0) # so that we can read from beginning
#     content = my_file.read()

#print(content)

# with open("files/data.txt", "a+") as data_file:
#     print(type(data_file))
#     data_file.seek(0)
#     content = data_file.read()
#     data_file.write("\n{}".format(content))
#     data_file.write("\n{}".format(content))

import time, os, pandas

while True:
    if os.path.exists("files/temps-today.csv"):
        data = pandas.read_csv("files/temps-today.csv")
        print(type(data))
        print(data.mean()["st1"])
    else:
        print("File does not exist!")
    time.sleep(5)

