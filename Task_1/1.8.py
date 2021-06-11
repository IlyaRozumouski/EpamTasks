a = int(input())
b = int(input())
c = int(input())
d = int(input())

for row in range(a, b + 1):
    for column in range(c, d + 1):
        print(row * column, end='\t')
    print()
