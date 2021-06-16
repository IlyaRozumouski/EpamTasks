def split_by_index(s, indexes):
    for elem in indexes:
        if elem > len(s):
            return "Bad index"
    word_list = list()
    word = ""
    i=0; j=0
    while i<len(s):
        if i == indexes[j]:
            word_list.append(word)
            word = ""
            word+=s[i]
            if j<len(indexes)-1:
                j+=1
        elif i == len(s)-1:
            word+=s[i]
            word_list.append(word)
        else:
            word+=s[i]
        i+=1
    return word_list

text = "Someverylongword"
indexes = [4,8,12]
print split_by_index(text,indexes)
