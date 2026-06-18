class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reverse_str_x = str_x[::-1]

        return str_x == reverse_str_x