class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, value):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def get(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node if node.is_end_of_word else None

class Homework(Trie):
    def __init__(self):
        super().__init__()
        self.words = set()  # Store inserted words to support suffix search

    def put(self, word, value):
        super().put(word, value)
        self.words.add(word)

    def count_words_with_suffix(self, pattern) -> int:
        return sum(word.endswith(pattern) for word in self.words)

    def has_prefix(self, prefix) -> bool:
        # Try to get keys with prefix if base Trie supports it
        node = self._get_node(prefix)
        return node is not None

    def _get_node(self, prefix):
        # Traverse the Trie nodes using the prefix
        node = self.root
        for char in prefix:
            # Now, use 'in' with TrieNode to check for child nodes
            if char not in node.children:  
                return None
            node = node.children[char]  # Move to the child node
        return node

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat", "category", "reservation"]
    for i, word in enumerate(words):
        trie.put(word, i)

    print("Перевірка кількості слів, що закінчуються на заданий суфікс:")
    print(trie.count_words_with_suffix("ion"))     
    print(trie.count_words_with_suffix("зo8n"))  
    print(trie.count_words_with_suffix("a"))     
    print(trie.count_words_with_suffix("cat"))    

    print("Перевірка наявності префікса:")
    print(trie.has_prefix("app"))  
    print(trie.has_prefix("bat")) 
    print(trie.has_prefix("ban"))  
    print(trie.has_prefix("ca"))  
