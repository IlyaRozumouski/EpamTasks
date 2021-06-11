txt = raw_input("Input some digits: ")
tuple = tuple(txt)
i=0
string = ""
while i < len(tuple):
    string = string+tuple[i]
    i = i+1
num = int(string)
print num