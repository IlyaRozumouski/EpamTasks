import string

#Function, used for adding unique letters 
def adding(string):
    dict={}
    for letter in string:
        dict[letter] = ""
    return dict.keys()

def fun1(list):
    print list
    alp = []
    for elem in list:
        alp+=adding(elem)
    i=0
    dict={}
    while i < len(alp):
        if alp.count(alp[i]) == len(list):
            dict[alp[i]] = alp[i]
        i+=1
    return dict.keys()

def fun2(list):
    print list
    alp = []
    for elem in list:
        alp += adding(elem)
    i=0
    dict = {}
    for elem in alp:
        dict[elem] = ""
    return dict.keys()

def fun3(list):
    print list
    alp = []
    for elem in list:
        alp += adding(elem)
    i=0
    dict={}
    while i < len(alp):
        if alp.count(alp[i]) >= 2:
            dict[alp[i]] = alp[i]
        i+=1
    return dict.keys()

def fun4(list):
    print list
    alp = []
    for elem in list:
        alp += adding(elem)
    for l in string.ascii_lowercase:
        alp.append(l)
    not_used = []
    for elem in alp:
        if alp.count(elem) == 1:
            not_used.append(elem)
    return not_used

list = ["hello", "world", "python"]
print fun1(list)
print fun2(list)
print fun3(list)
print fun4(list)