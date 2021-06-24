class HistoryDict:
    history = list()
    def __init__(self, dict = dict()):
        self.dict = dict
    def set_value(self, dict = dict()):
        self.dict[dict.keys()[0]] = dict.values()[0]
    def get_history(self):
        sorted_by_value = sorted(self.dict.items(), key=lambda kv: kv[1])
        sorted_by_value.reverse()
        i = 0
        while i < 10:
            self.history.append(sorted_by_value[i][0])
            i+=1
        print self.history

d=HistoryDict({"boo":1})
d.set_value({"foo":2})
d.set_value({"loo":3})
d.set_value({"woo":4})
d.set_value({"doo":5})
d.set_value({"coo":6})
d.set_value({"roo":7})
d.set_value({"moo":8})
d.set_value({"noo":9})
d.set_value({"soo":10})
d.set_value({"koo":11})
d.set_value({"deer":12})
d.get_history()
