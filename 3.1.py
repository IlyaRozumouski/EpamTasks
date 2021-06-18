list = []
with open("C:\Users\Admin\PycharmProjects\Tasks\data\unsorted_names.txt") as file:
    string = str(file.read())
    list = string.split("\n")
    list.sort()
    del list[0]
with open('sorted_names.txt', 'w') as f:
    for elem in list:
        f.write(elem+"\n")
