from trie import Trie, TrieNode

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        self.root = TrieNode()
        for string in strings:
            self.put(string, True)

        current = self.root
        path = ''
        while len(current.children) == 1:
            char = next(iter(current.children))
            path += char
            current = current.children[char]

        return path

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""