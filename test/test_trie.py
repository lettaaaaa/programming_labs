import unittest
from src.trie import TrieNode, Trie, build_trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.patterns = ["code", "cob", "bc", "xyz"]
        self.trie = build_trie(self.patterns)

    def test_search_existing_word(self):
        self.assertTrue(self.trie.search("code"))
        self.assertTrue(self.trie.search("cob"))

    def test_search_non_existing_word(self):
        self.assertFalse(self.trie.search("abc"))

    def test_starts_with_prefix(self):
        self.assertTrue(self.trie.startsWith("co"))
        self.assertTrue(self.trie.startsWith("x"))

    def test_starts_with_non_prefix(self):
        self.assertFalse(self.trie.startsWith("ab"))


if __name__ == '__main__':
    unittest.main()
