def get_longest_word(string):
    list = string.split()
    longest_word = ""
    for elem in list:
        if len(elem)>len(longest_word):
            longest_word = elem
    return longest_word

txt = raw_input("Input text: ")
print get_longest_word(txt)