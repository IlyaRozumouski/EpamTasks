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
