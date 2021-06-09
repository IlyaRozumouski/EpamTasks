print "Input any digit"
x=input()
var=1
list = []
while var<=x:
    if x%var == 0:
        list.append(var)
    var = var+1
print list