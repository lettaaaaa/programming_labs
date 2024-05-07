class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def build_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie

"""
patterns = ["code", "cob", "bc", "xyz"]
trie = build_trie(patterns)

print(trie.search("code"))  # True
print(trie.search("cob"))  # True
print(trie.startsWith("co"))  # True
print(trie.startsWith("x"))  # True
print(trie.search("abc"))  # False"""
