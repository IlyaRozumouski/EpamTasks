def foo(list):
    new_list = []
    max_value = 1
    for elem in list:
        max_value *= elem
    for elem in list:
        new_elem = max_value/elem
        new_list.append(new_elem)
    return new_list

list = list(input("Input variables: "))
print foo(list)