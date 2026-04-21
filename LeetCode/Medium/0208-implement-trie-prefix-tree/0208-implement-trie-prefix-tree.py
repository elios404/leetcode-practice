"""
1. Approach
    - Implement basic trie data structure.
2. Time Complexity : O(N) - only linear scan for `word` or `prefix` and inside while loop takes O(1)
3. Space Complexity : O(N * M * (26)) - word letter N and number of words M and children for each alphabets
"""
class TrieNode:
    def __init__(self):
        # Pythonic: Hash map (dict) instead of size-26 array.
        # Maps a character directly to its child TrieNode.
        self.children = {} 
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        # Pythonic: Iterate directly over the string (No deque needed, O(1) space)
        for char in word:
            # If the character isn't a child yet, create it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move down the tree
            curr = curr.children[char]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        # Only true if we finished exactly at a word boundary
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        # If we didn't return False during the loop, the prefix exists!
        return True