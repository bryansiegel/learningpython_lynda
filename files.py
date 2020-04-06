# Open a file
# f = open("textfile.txt", "w+")

# append to end of file
# f = open("textfile.txt", "a")

f = open("textfile.txt", "r")

if f.mode == 'r':
    contents = f.read()
    print(contents)



# for i in range(100):
#     f.write("this is line " + str(i) + "\r\n")

# f.close()
