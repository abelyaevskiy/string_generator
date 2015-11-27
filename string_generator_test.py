import unittest
from string_generator import StringGenerator


class MyTestCase(unittest.TestCase):

    def testStringGeneratorObjectIsEmpty(self):
        gen = StringGenerator()
        self.assertEqual(gen.build(), '')

    def testWithTermMethodsAddsTerms(self):
        gen = StringGenerator()
        gen.term('brown').term('fox')
        self.assertEquals(gen.terms, {'brown': {'count': 1, 'shuffle': False}, 'fox': {'count': 1, 'shuffle': False}})

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

    def testCreateStringWithPrefixedTerms(self):
        gen = StringGenerator()
        s = gen.random_term_of_length(5).prefix('abc').repeat(10).build()
        words = s.split()
        self.assertEquals(s.count(' '), 9)
        self.assertEquals(words.count(), 10)
        for word in words:
            self.assertEquals(word.count, 5)
            self.assertEquals(word.startswith('abc'))


if __name__ == '__main__':
    unittest.main()
