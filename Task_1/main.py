# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def strlen(txt):
    count=0
    for char in txt:
        count+=1
    return count

txt = raw_input("Введите строку: ")

print "Символов:", strlen(txt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/