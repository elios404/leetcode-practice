class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        steps = [0 for i in range(n+1)]
        steps[0], steps[1] = 1, 1

        for i in range(2, n+1):
            steps[i] = steps[i-2] + steps[i-1]

        return steps[n]