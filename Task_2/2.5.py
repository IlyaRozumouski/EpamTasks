def get_digits(num):
    txt = str(num)
    return tuple(txt)

number = int(input("Input number: "))
print get_digits(number)