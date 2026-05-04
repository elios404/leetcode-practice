"""
import dataclasses

@dataclasses.dataclass
class Node:
    isEnd: bool
    child: dict = dataclasses.field(dict)
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        # We will cache the top 3 lexicographically smallest words right here!
        self.suggestions = [] 

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 1. Sort products first. This guarantees lexicographical order globally.
        products.sort()

        root = TrieNode()
        
        # 2. Build the Trie and cache suggestions on the fly
        for product in products:
            curr = root
            for char in product:
                # Pythonic: dict.setdefault creates the node if it doesn't exist
                curr = curr.children.setdefault(char, TrieNode())
                
                # Because we sorted first, the first 3 words to reach this node
                # are mathematically guaranteed to be the top 3 smallest!
                if len(curr.suggestions) < 3:
                    curr.suggestions.append(product)

        # 3. Search Phase (Lightning Fast)
        ans = []
        curr = root
        
        for char in searchWord:
            if curr: # If we haven't hit a dead end
                curr = curr.children.get(char) # Safe lookup, returns None if char not found
            
            # If curr exists, append its cached suggestions. Otherwise, append empty list.
            ans.append(curr.suggestions if curr else [])

        return ans