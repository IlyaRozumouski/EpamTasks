def most_common_words(path="C:\Users\Admin\PycharmProjects\Tasks\data\lorem_ipsum.txt",amount=3):
    with open(path) as file:
        stri = str(file.read())
        stri = stri.lower()
        le = list(stri)
        for letter in le:
            if letter == "." or letter == ",":
                le.remove(letter)
        string = str()
        for letter in le:
            string+=letter
        lst = string.split()
        common_elements = []
        i=0
        while i < amount:
            max_count = 0
            word = str()
            for elem in lst:
                if lst.count(elem) > max_count and common_elements.count(elem) == 0:
                    max_count = lst.count(elem)
                    word = elem
            common_elements.append(word)
            i+=1
        print common_elements

most_common_words()