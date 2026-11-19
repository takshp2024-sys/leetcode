class TrieNode:
    def __init__(self):
        # A dictionary to store children nodes
        self.children = {}
        # A boolean flag to indicate if this node marks the end of a word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # The root of the Trie is an empty TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            # If the character is not in the current node's children, add it
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the next node
            current = current.children[char]
        # Mark the end of the word
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            # If the character is not found, the word doesn't exist
            if char not in current.children:
                return False
            current = current.children[char]
        # Return True only if we reached the end of the word AND it's marked as a complete word
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            # If the character is not found, no word has this prefix
            if char not in current.children:
                return False
            current = current.children[char]
        # If we successfully traversed the prefix, return True
        return True