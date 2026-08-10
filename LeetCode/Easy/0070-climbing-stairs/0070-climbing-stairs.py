class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        two_step, one_step = 1, 1
        for i in range(2, n+1):
            step = two_step + one_step
            two_step, one_step = one_step, step

        return step