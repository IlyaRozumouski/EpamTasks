def strlen(abc):
    count=0
    for i in abc:
        count+=1
    return count

txt = raw_input("Input string: ")

print "Symbols: ", strlen(txt)