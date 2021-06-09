dictionary = {}
string = raw_input("Input string: ")
for ch in string.lower():
    keys = dictionary.keys()
    if ch in keys:
        dictionary[ch] += 1
    else:
        dictionary[ch] = 1
print dictionary