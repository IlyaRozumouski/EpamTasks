# Task 3.5 decorator
def previous(func):
    with open("prev.txt", "r") as file:
        variable = file.read()

    def wrapper_prev(*args):
        nonlocal variable
        print("The previous result is: ", variable)
        variable = func(*args)
        with open("prev.txt", "w") as file:
            file.write(str(variable))
    return wrapper_prev


# Task 3.6 decorator
def call_once(func):
    variable = 0

    def wrap(*args):
        nonlocal variable
        if variable == 0:
            variable = func(*args)
        print("Cache is: ", variable)
    return wrap
