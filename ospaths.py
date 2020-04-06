import os
from os import path
import datetime
from datetime import date, time,timedelta
import time

print(os.name)

# print("item exists" + str(path.exists("textfile.txt")))
# print("item is a file " + str(path.isfile("textfile.txt")))
# print("item is a directory " + str(path.isdir("textfile.txt")))

# get file full path
# print("item real path is " + str(path.realpath("textfile.txt")))
# print("item and path name" + str(path.split(path.realpath("textfile.txt"))))


# t = time.ctime(path.getmtime("textfile.txt"))
# print(t)
#
# print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

# How long ago was file modified
td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

print("it has been " + str(td) + " since the file was last modified")
print("or, " + str(td.total_seconds()) + " seconds")