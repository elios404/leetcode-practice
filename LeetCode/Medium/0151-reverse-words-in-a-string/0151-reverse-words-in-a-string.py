"""
1. Approach
    - Tokenize the input string into a list of words using default whitespace splitting.
    - Reverse the sequence of the parsed words and concatenate them using a single space delimiter.
2. Time complexity : O(N) - Although the built-in functions perform multiple linear passes(split, reverse, join) resulting O(3N), we drop the constants to simplify the overall time complexity to O(N)
3. Space Complexity : O(N) - We allocate auxiliary space to store the list of parsed words.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
        