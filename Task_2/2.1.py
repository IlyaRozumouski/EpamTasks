def function1(string):
    return string.replace('\"', "\'")
def function2(string):
    return string[::-1]

text = raw_input("Input text: ")
print function2(function1(text))