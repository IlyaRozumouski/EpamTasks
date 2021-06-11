list = [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"}, {"VI" : "S005"}, {"VII" : "S005"}, {"V" : "S009"}, {"VIII" : "S007"}]
i=0
new_list = []
while i<len(list):
    count = 0
    string = ""
    ii = 0
    while ii<len(str(list[i])):
        abc = str(list[i])
        if abc[ii] == "'":
            count+=1
        if count == 3:
            string+=abc[ii]
        ii+=1
    string = string[1:]
    if new_list.count(string) == 0:
        new_list.append(string)
    i+=1
print list
print new_list
# [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]