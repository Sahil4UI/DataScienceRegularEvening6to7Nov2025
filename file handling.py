data = '''Python Features:
1.High Level
2.General Purpose
3.Multi Paradigm
4.interpreted programming'''

# FILE HANDELING
# file = open("data.txt",mode="w")
# file.write(data)
# file.close()

# with open("data.txt",mode="w") as file:
#     file.write(data)

# with open("data.txt",mode="a") as file:
#     file.write("\n6.Platform Independent")

with open("data.txt",mode="r") as file:
    # data = file.read()
    # data = file.read(3)
    # data = file.readline()#first line
    data = file.readlines()
    for line in data:
        print(line)
