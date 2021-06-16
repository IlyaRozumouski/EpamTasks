def combine_dicts(*args):
    dictionary = {}
    list_of_indexes = []
    list_of_values = []
    for elem in args:
        list_of_indexes+=elem.keys()
        list_of_values+=elem.values()
    i=0;j=1
    while i<len(list_of_indexes):
        while j<len(list_of_indexes):
            if list_of_indexes[i] == list_of_indexes[j]:
                list_of_values[i] += list_of_values[j]
                del list_of_indexes[j]
                del list_of_values[j]
            j+=1
        i+=1
    i=0
    while i<len(list_of_indexes):
        dictionary[list_of_indexes[i]] = list_of_values[i]
        i+=1
    return dictionary

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print combine_dicts(dict_1,dict_2,dict_3)