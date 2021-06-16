def get_pairs(list):
    if len(list)>1:
        i=0; j=1
        out = []
        while i < len(list) and j < len(list):
            tuple = (list[i],list[j])
            out.append(tuple)
            i+=1; j+=1
        return out
list = list(raw_input("Input list: "))
print get_pairs(list)