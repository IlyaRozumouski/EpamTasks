class Pagination:
    def __init__(self, text, size):
        self.text = text
        self.pages = list()
        i = 0
        string = ""
        for elem in text:
            string += elem
            if i % size == 0 and i != 0:
                self.pages.append(string)
                string = ""
            elif i == len(text) - 1:
                self.pages.append(string)
            i += 1

    def item_count(self):
        return len(self.text)

    def pages_count(self):
        return len(self.pages)

    def count_items_on_page(self, num):
        try:
            print(len(self.pages[num]))
        except IndexError:
            raise IndexError("Invalid index. Page is missing")

    def search(self, text):
        d = {}
        i = 0
        for elem in self.pages:
            if elem.find(text) != -1:
                d[i] = elem.find(text)
            i += 1
        if len(d) == 0:
            raise Exception(f'{text} is missing on pages')
        else:
            print(d)


pages = Pagination("Your beautiful text", 5)
pages.count_items_on_page(2)
print(pages.pages)
pages.search("t")
