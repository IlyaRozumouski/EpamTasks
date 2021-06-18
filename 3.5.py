from decorators import previous


@previous
def sum_list(*args):
    if type(args[0]) == str:
        result = str()
        for item in args:
            result += item
        print("The present result is: ", result)
        return result
    if type(args[0]) == int:
        result = 0
        for item in args:
            result += item
        print("The present result is: ", result)
        return result


sum_list("Somebody", " once", " told me")
