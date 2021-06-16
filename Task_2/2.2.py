def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

txt = raw_input("Input string: ")
print(is_palindrome(txt))
