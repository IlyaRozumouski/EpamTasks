def diysplit(string, splitcase = " "):
    num = 0
    for i in string:
        if i == splitcase:
            num+=1
    word_list = list()
    word = ""
    count = 0
    for i in string:
        if i == splitcase:
            word_list.append(word)
            word = ""
            count+=1
        elif count == num:
            iter = string.index(i)
            while iter<len(string):
                word+=string[iter]
                iter+=1
            word_list.append(word)
            break
        else:
            word+=i
    return word_list

txt = raw_input("Input text: ")
print diysplit(txt)