exchange_rate = {
    "USD": 2.53,
    "EUR": 3.02,
    "RUB": 0.0349,
    "BYN": 1
}


def exchange(money, arg="USD"):
    value = float(list(money.cash.values())[0])
    return {arg: round(value / exchange_rate[arg], 3)}


def get_own_currency(money):
    exchange_value = exchange_rate[list(money.keys())[0]]
    return {"BYN": exchange_value * list(money.values())[0]}


class Currency:
    def __init__(self, amount=0, currency="BYN"):
        self.value = amount
        self.currency = currency
        self.cash = {self.currency: self.value}

    def __add__(self, other):
        return {"BYN": round(float(list(get_own_currency(self.cash).values())[0])
                             + float(list(get_own_currency(other.cash).values())[0]), 5)}

    def __sub__(self, other):
        return {"BYN": round(float(list(get_own_currency(self.cash).values())[0])
                             - float(list(get_own_currency(other.cash).values())[0]), 5)}

    def __mul__(self, other):
        return {"BYN": round(float(list(get_own_currency(self.cash).values())[0])
                             * float(list(get_own_currency(other.cash).values())[0]), 5)}

    def __truediv__(self, other):
        return {"BYN": round(float(list(get_own_currency(self.cash).values())[0])
                             / float(list(get_own_currency(other.cash).values())[0]), 3)}

    def __cmp__(self, other):
        if float(list(get_own_currency(self.cash).values())[0]) \
                == float(list(get_own_currency(other.cash).values())[0]):
            return True
        else:
            return False


a = Currency(10)
b = Currency(10, "USD")
print(exchange(a))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a == b)

