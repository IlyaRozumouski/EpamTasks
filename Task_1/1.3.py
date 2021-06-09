dictionary = dict()
def func1(abc):

    for i in abc:
        dictionary[i] = 1

txt = input("Input string: ")
func1(txt)
print dictionary