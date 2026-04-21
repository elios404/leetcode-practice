"""
1. Approach
    - Implement basic trie data structure.
2. Time Complexity : O(N) - only linear scan for `word` or `prefix` and inside while loop takes O(1)
3. Space Complexity : O(N * M * (26)) - word letter N and number of words M and children for each alphabets
"""
from collections import deque

class Node:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if not word:
            return
        cur_node = self.root
        word_q = deque(word) # O(N)?

        # O(N)
        while word_q: #There are letters remained
            char = word_q.popleft()
            idx = ord(char.lower()) - ord('a')
            if not cur_node.children[idx]: # if it was None
                cur_node.children[idx] = Node()
            cur_node = cur_node.children[idx]
        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        if not word:
            return False

        cur_node = self.root
        word_q = deque(word)
        
        # O(N)
        while word_q:
            if not cur_node:
                return False
            char = word_q.popleft()
            idx = ord(char.lower()) - ord('a')
            if not cur_node.children[idx]: # if it was None
                return False # no such pattern
            cur_node = cur_node.children[idx]
        
        if cur_node.isEnd:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False

        cur_node = self.root
        prefix_q = deque(prefix)
        
        # O(N)
        while prefix_q:
            if not cur_node:
                return False
            char = prefix_q.popleft() # O(1)
            idx = ord(char.lower()) - ord('a')
            if not cur_node.children[idx]: # if it was None
                return False # no such pattern
            cur_node = cur_node.children[idx]
        
        return True
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)