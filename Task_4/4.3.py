import string


class Cipher:

    def __init__(self, s=""):
        self.cipher_string = s.lower()

    def __generate_encryption_alphabet(self):
        letters = list(self.cipher_string)
        letters.reverse()
        for elem in letters:
            if letters.count(elem) > 1 or elem == " ":
                del letters[letters.index(elem)]
        letters.reverse()
        unsorted_alp = ""
        for elem in letters:
            unsorted_alp += elem
        unsorted_alp += string.ascii_lowercase
        letters = list(unsorted_alp)
        letters.reverse()
        for elem in letters:
            if letters.count(elem) > 1:
                del letters[letters.index(elem)]
        out = ""
        letters.reverse()
        for elem in letters:
            out += elem
        return out

    def encode(self, word):
        if self.cipher_string == "":
            return "Cypher word is not defined"
        encryption_list = list(self.__generate_encryption_alphabet())
        normal_letters = list(string.ascii_lowercase)
        word = word.lower()
        encryption_word = ""
        for elem in word:
            index = normal_letters.index(elem)
            encryption_word += encryption_list[index]
        return encryption_word

    def decode(self, encryption_word):
        if self.cipher_string == "":
            return "Cypher word is not defined"
        encryption_list = list(self.__generate_encryption_alphabet())
        normal_letters = list(string.ascii_lowercase)
        encryption_word = encryption_word.lower()
        word = ""
        for elem in encryption_word:
            index = encryption_list.index(elem)
            word += normal_letters[index]
        return word


c = Cipher("Hello World")
print(c.encode("Son"))
print(c.decode(c.encode("Son")))
