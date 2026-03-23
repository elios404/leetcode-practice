"""
1. Approach
    - choose one index which exactly what the same sum value fromt left and right
2. Time Complexity : O(N) - Scan whole list to get total sum valuem, and linear traversal of nums to check whether left sum and right sum is equal.
3. Space Complexity : O(1) - Constant auxiliary space for left_sum and right_sum
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(num for num in nums) #O(N)

        # O(N)
        for i in range(len(nums)):
            right_sum -= nums[i]
            # check if `i` can seperate left and right into same sum value
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1
        