from trie import Trie, TrieNode

class Homework(Trie):
    def __init__(self):
        super().__init__()
        self.root_reversed = TrieNode()

    def put(self, key, value=None):
        # make 2 trie for prefix and suffix
        def _put(root, key):
            if not isinstance(key, str) or not key:
                raise TypeError(f"Illegal argument for put: key = {key} must be a non-empty string")

            current = root
            for char in key:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            if current.value is None:
                self.size += 1
            current.value = value

        _put(self.root, key)
        _put(self.root_reversed, key[::-1])

    def count_words_with_suffix(self, pattern) -> int:
        pattern = pattern[::-1]
        if not isinstance(pattern, str):
            raise TypeError(f"Illegal argument for count_words_with_suffix: suffix = {pattern} must be a string")

        current = self.root_reversed
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]

        result = []
        self._collect(current, list(pattern), result)
        return len(result)        

    def has_prefix(self, prefix) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat