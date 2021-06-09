dictionary = {"5":3, "3":2,"6":1, "2":5, "1":6}
list_keys = list(dictionary.keys())
list_keys.sort()
for i in list_keys:
    print(i, ':', dictionary[i])