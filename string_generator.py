import collections
import random
import string


class StringGenerator:
    def __init__(self):
        self.file = 'dummy_voc.txt'
        self.terms = collections.OrderedDict()
        self.row = ''
        self.current_term = ''
        self.size = 0
        self.termsForString = []
        self.isShuffle = False
        self.isCurrentTermRandom = False

    def term(self, term):
        self.terms[term] = {'count': 1, 'shuffle': False}
        self.current_term = term
        self.isCurrentTermRandom = False
        self.size += 1
        return self

    def repeat(self, count):
        self.terms[self.current_term]['count'] = count
        self.size += count-1
        return self

    def shuffle(self):
        self.terms[self.current_term]['shuffle'] = True
        self.isShuffle = True
        return self

    def random_term_of_length(self, length):
        self.current_term = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        self.isCurrentTermRandom = True
        return self

    def prefix(self, prfx):
        return self

    def build(self):
        for term, params in self.terms.items():
            for i in range(0, params['count']):
                self.termsForString.append(term)
        if self.isShuffle:
            random.shuffle(self.termsForString)
        for term in self.termsForString:
            self.row += term + ' '
        self.row = self.row[:-1]

        return self.row
