class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.Node()
            node = node.children[char]
        node.is_end = True


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        # Вставити всі слова в Trie
        for word in strings:
            self.insert(word)

        # Пошук спільного префікса
        prefix = ""
        node = self.root

        while len(node.children) == 1 and not node.is_end:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]

        return prefix


if __name__ == "__main__":
    examples = [
        (["flower", "flow", "flight"], "fl"),
        (["interspecies", "interstellar", "interstate"], "in"),
        (["dog", "racecar", "car"], "")
    ]

    for strings, expected in examples:
        trie = LongestCommonWord()
        result = trie.find_longest_common_word(strings)
        print(f"Вхідні рядки: {strings}")
        print(f"Очікувано: '{expected}', Отримано: '{result}'")
        print(f"Результат: {'✅ Успіх' if result == expected else '❌ Невірно'}")

        print("-" * 50)
