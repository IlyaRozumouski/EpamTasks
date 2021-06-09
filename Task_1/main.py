# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def strlen(abc):
    count=0
    for i in abc:
        count+=1
    return count

txt = raw_input("Input string: ")

print "Symbols: ", strlen(txt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
