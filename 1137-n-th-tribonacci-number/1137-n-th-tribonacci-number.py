"""
1. Approach : Change normal fibonacci a bit.
2. Time Complexity : O(N) - while loop runs until N
3. Space Comeplxity : O(1) - In this code we don't need to save all values of tribonacci, just need n, n+1, n+2 three values. So use constant variable means constant auxiliary space.
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n in [1,2]:
            return 1

        num1, num2, num3 = 0,1,1

        i = 3
        while i <= n :
            num1, num2, num3 = num2, num3, num1+num2+num3
            i += 1

        return num3