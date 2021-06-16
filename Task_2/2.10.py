def generate_squares(num):
    i=1
    squares = {}
    while i<=num:
        squares[i] = i*i
        i+=1
    return squares

print generate_squares(5)