import unittest
from src.WCHAIN import longest_word_chain


class TestLongestWordChain(unittest.TestCase):
    def test_example_case(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        expected_output = 6
        self.assertEqual(longest_word_chain(words), expected_output)

    def test_case_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        expected_output = 4
        self.assertEqual(longest_word_chain(words), expected_output)

    def test_case_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        expected_output = 1
        self.assertEqual(longest_word_chain(words), expected_output)


if __name__ == '__main__':
    unittest.main()
