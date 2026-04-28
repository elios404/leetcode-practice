class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret = 0
        while a != 0 or b != 0 or c != 0:
            a_right, b_right, c_right = a%2, b%2, c%2
            ab = a_right|b_right
            if ab != c_right: # need to change
                if a_right == 1 and b_right == 1:
                    ret += 2
                else:
                    ret += 1
            a, b, c = a//2, b//2, c//2
        
        return ret