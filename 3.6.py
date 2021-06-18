from decorators import call_once


@call_once
def sum_of_numbers(a, b):
    return a + b


sum_of_numbers(3, 7)
sum_of_numbers(4, 3)
sum_of_numbers(3, 13)
