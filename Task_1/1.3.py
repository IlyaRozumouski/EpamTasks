list = []
list = input("Input string: ")
new_list = []
for elem in list:
     if list.count(elem)>=2:
          continue
     else:new_list.append(elem)
new_list.sort()
print new_list

#['red', 'white', 'black', 'red', 'green', 'black']



