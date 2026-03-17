"""
1. Approach
    - iterate the input string s and split the string with ' '
    - Reverse the list and join it with ' '
2. Time complexity : O(N) - Scan string `s` once, and make it reverse, join the list -> O(3*N)?
3. Space Complexity : O(N) - auxiliary space O(N) needed to save reversed word List.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip().split(" ")[::-1]
        # a bit weird solution isn't it..?
        return " ".join(word for word in l if word != '')
        