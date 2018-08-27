import string

# O(n) time and O(n) space
class WordCloud:
    # Write code that takes a long string and builds its word cloud data in a dictionary,
    # where the keys are words and the values are the number of times the words occurred.

    # I use a subset of C locale definition of string.punctuation so as to allow for hyphenated-words:
    # string.punctuation == """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    punctuation = set(string.punctuation)
    punctuation.remove('-')

    @staticmethod
    def strip_punctuation(string: str):
        chars = list(string)
        stripped_chars = []
        for c in chars:
            if c not in WordCloud.punctuation:
                stripped_chars.append(c)

        return ''.join(stripped_chars)

    def __init__(self, string: str):
        self.string = self.stripped_string = None
        self.word_cloud = {}
        self.set_string(string)

    def set_string(self, string: str):
        self.string = string
        self.stripped_string = WordCloud.strip_punctuation(string.lower())
        self.__calculate()

    def __calculate(self):
        self.word_cloud.clear()
        words = self.stripped_string.split()
        for word in words:
            if word in self.word_cloud:
                self.word_cloud[word] += 1
            else:
                self.word_cloud[word] = 1
