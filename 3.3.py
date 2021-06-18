def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path) as file:
        s = file.read().split("\n")
        list = []
        for elem in s:
            list.append(elem.split(","))
        del list[0]
        i=0
        out=[]
        while i<number_of_top_students:
            max_average_mark = 0.0
            name = ""
            for elem in list:
                if elem[2]>max_average_mark and out.count(elem[0]) == 0:
                    max_average_mark = elem[2]
                    name = elem[0]
            out.append(name)
            i+=1
        print out

def descending_age(file_path):
    with open(file_path) as file:
        s = file.read().split("\n")
        list = []
        for elem in s:
            list.append(elem.split(","))
        out = []
        out.append(list[0])
        del list[0]
        list = sorted(list,key=lambda person: person[1])
        list.reverse()
        out+=list
        with open('descending_age.csv', 'w') as f:
            f.write("student name,age,average mark\n")
            for elem in list:
                f.write(elem[0] + ", " + elem[1] + ", " + elem[2] +"\n")
descending_age("C:\Users\Admin\PycharmProjects\Tasks\data\students.csv")
get_top_performers("C:\Users\Admin\PycharmProjects\Tasks\data\students.csv")
