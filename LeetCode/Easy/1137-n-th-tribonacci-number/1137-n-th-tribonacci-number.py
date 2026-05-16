"""
1. Approach : Change normal fibonacci a bit.
2. Time Complexity : O(N) - while loop runs until N
3. Space Comeplxity : O(1) - In this code we don't need to save all values of tribonacci, just need n, n+1, n+2 three values. So use constant variable means constant auxiliary space.
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        num1, num2, num3 = 0,1,1

        for _ in range(3, n + 1):
            num1, num2, num3 = num2, num3, num1 + num2 + num3

        return num3