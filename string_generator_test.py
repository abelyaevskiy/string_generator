import unittest
from string_generator import StringGenerator


class MyTestCase(unittest.TestCase):

    def testSingleTermRepeatedGivenNumberTimes(self):
        gen = StringGenerator()
        self.assertEquals(gen.term('brown').repeat(3).build(), 'brown brown brown')

    def testSomeTermsRepeatGivenNumber(self):
        gen = StringGenerator()
        s = gen.term('brown').repeat(2).term('fox').repeat(3).term('jump').repeat(4).build()
        self.assertEquals(s, 'brown brown fox fox fox jump jump jump jump')

    def testSomeTermsRepeatedGivenNumTimesInShuffleOrder(self):
        gen = StringGenerator()
        s = gen.term('brown').repeat(2).term('fox').repeat(3).term('jump').repeat(4).shuffle().build()
        self.assertNotEquals(s, 'brown brown fox fox fox jump jump jump jump')
        self.assertEquals(s.count('brown'), 2)
        self.assertEquals(s.count('fox'), 3)
        self.assertEquals(s.count('jump'), 4)
        self.assertEquals(s.count(' '), 8)

    def testCreateStringBasedOnRandomTermWithFixedPrefix(self):
        gen = StringGenerator()
        s = gen.random_term(5).prefix_fixed('abc').repeat(10).build()
        words = s.split()
        self.assertEquals(s.count(' '), 9)
        self.assertEquals(len(words), 10)
        for word in words:
            self.assertEquals(len(word), 8)
            self.assertEquals(word.startswith('abc'), True)

    def testCreateStringBaseOnFixedTermWithFixedPrefix(self):
        gen = StringGenerator()
        s = gen.term('brown').prefix_fixed('abc').repeat(4).build()
        self.assertEquals(s, 'abcbrown abcbrown abcbrown abcbrown')

    def testStringWithIncreasingPrefix(self):
        gen = StringGenerator()
        s = gen.term('t').prefix_inc('a').repeat(4).build()
        self.assertEquals(s, 'at aat aaat aaaat')

    # def testBigString(self):
    #     gen = StringGenerator()
    #     s = gen.term('brown').repeat(1000).
    #             term('fox').

    def testStringWith2RepeatByEachTerms(self):
        gen = StringGenerator()
        s = gen.term('word').repeat(10).term('fox').prefix_inc('z').each(3).term('jump').each(5).build()
        self.assertEquals(s, 'word word zfox word jump zafox word word zabfox jump word zabcfox word word zabcdfox word word')

    def testAlphabetIncrementalPrefixGoesBeyondZShouldCycleFromA(self):
        gen = StringGenerator()
        s = gen.term('dummy').prefix_alphinc('z').repeat(2).build()
        self.assertEquals(s, 'zdummy zadummy')

    def testAddFixedPrefixForWordsFromGivenString(self):
        gen = StringGenerator('red fox jump over lazy dog')
        s = gen.prefix('a').build()
        self.assertEquals(s, 'ared afox ajump aover alazy adog')

    def testAddIncPrefixForWordsFromGivenString(self):
        gen = StringGenerator('red fox jump over lazy dog')
        s = gen.prefix_inc('a').build()
        self.assertEquals(s, 'ared aafox aaajump aaaaover aaaaalazy aaaaaadog')

    def testAddAlphaIncPrefixForWordsFromGivenString(self):
        gen = StringGenerator('red fox jump over lazy dog')
        s = gen.prefix_alphinc('z').build()
        self.assertEquals(s, 'zred zafox zabjump zabcover zabcdlazy zabcdedog')

    def testAddDifferentPrefixForWordsFromGivenString(self):
        gen = StringGenerator('red fox jump')
        s = gen.prefix('a').prefix_inc('c').prefix_alphinc('o').build()
        self.assertEquals(s, 'ared cred ored afox ccfox opfox ajump cccjump opqjump')

    # 'a<rand_term_1> a<rand_term_2> a<rand_term_3> a<rand_term_4> a<rand_term_5> a<rand_term_6>'
    # '<rand_pref_1>a <rand_pref_2>a <rand_pref_3>a'


if __name__ == '__main__':
    unittest.main()
