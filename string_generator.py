import collections
import random
import string
from enum import Enum


class PrefixType(Enum):
    no_prefix = 0
    fixed = 1
    simple_inc = 2
    alph_inc = 3


class StringGenerator:
    def __init__(self):
        self.terms = collections.OrderedDict()
        self.term_count = 0
        self.termsForString = []
        self.isShuffle = False
        self.row = ''
        self.current_term = ''
        self.term_position_map = {}

    def term(self, term):
        self.current_term = term
        self.add_term()
        return self

    def random_term(self, length):
        self.current_term = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        self.add_term()
        return self

    def add_term(self):
        self.terms[self.current_term] = {
            'count': 1,
            'current_counter': 0,
            'shuffle': False,
            'prefix': '',
            'prefix_type': PrefixType.no_prefix
        }
        self.term_count += 1

    def repeat(self, count):
        self.terms[self.current_term]['count'] = count
        self.term_count += count - 1
        return self

    def each(self, repeat_multiplier):
        self.term_position_map[repeat_multiplier] = self.current_term
        return self

    def shuffle(self):
        self.terms[self.current_term]['shuffle'] = True
        self.isShuffle = True
        return self

    def prefix_fixed(self, prfx):
        self.prefix(prfx, PrefixType.fixed)
        return self

    def prefix_inc(self, prfx):
        self.prefix(prfx, PrefixType.simple_inc)
        return self

    def prefix_alphinc(self, prfx='a'):
        self.prefix(prfx, PrefixType.alph_inc)
        return self

    def prefix(self, prfx, prfx_t):
        self.terms[self.current_term]['prefix'] = prfx
        self.terms[self.current_term]['prefix_type'] = prfx_t

    def build(self):
        if self.term_position_map == {}:
            for term, params in self.terms.items():
                while params['current_counter'] < params['count']:
                    prefix = self.build_prefix(term, params)
                    self.termsForString.append(prefix + term)
                    self.terms[term]['current_prefix'] = prefix
                    self.terms[term]['current_counter'] += 1
        else:
            positions = self.term_position_map.keys()
            term_counter = 0
            global_counter = 0
            while term_counter < len(self.terms):
                pos = self.get_first_delim_from_list(positions, global_counter + 1)
                if pos:
                    term = self.term_position_map[pos]
                else:
                    term = list(self.terms.items())[term_counter][0]
                prefix = self.build_prefix(term, self.terms[term])
                self.termsForString.append(prefix + term)
                self.terms[term]['current_counter'] += 1
                if self.terms[term]['current_counter'] == self.terms[term]['count']:
                    term_counter += 1
                global_counter += 1

        if self.isShuffle:
            random.shuffle(self.termsForString)
        for term in self.termsForString:
            self.row += term + ' '
        self.row = self.row[:-1]
        return self.row

    def build_prefix(self, term, params):
        prefix_type = params['prefix_type']
        if prefix_type == PrefixType.alph_inc:
            if params['current_counter'] == 0:
                prefix = params['prefix']
            else:
                term_current_prefix = self.terms[term]['current_prefix']
                last_char = term_current_prefix[-1]
                if last_char == 'z':
                    next_char = 'a'
                else:
                    next_char = chr(ord(last_char) + 1)
                prefix = term_current_prefix + next_char
            self.terms[term]['current_prefix'] = prefix
        elif prefix_type == PrefixType.simple_inc:
            prefix = params['prefix'] * (params['current_counter'] + 1)
        elif prefix_type == PrefixType.fixed:
            prefix = params['prefix']
        else:
            prefix = ''
        return prefix

    @staticmethod
    def get_first_delim_from_list(positions, tc):
        pos = False
        for i in positions:
            if tc % i == 0:
                pos = i
                break
        return pos


class String:
    def __init__(self):
        self.size = 0
        self.length = 0
        self.words_count = 0
        self.space_count = 0
        self.space = ' '
        self.term_builders = collections.OrderedDict()
        self.result_string = ''

    def build(self):

        return self.result_string


class Term:
    def __init__(self):
        self.size = 0
        self.length = 0
        self.term = ''

    def build(self):
        return self.term