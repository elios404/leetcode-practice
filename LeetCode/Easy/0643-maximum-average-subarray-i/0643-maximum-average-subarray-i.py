"""
1. Approach
    - Need to calculate subarray's mean value, also can just calculate sum value and divide it into `k` in the end
    - Check from 0 to k and move the window through the array
2. Time Complexity : O(N) - To find sum value, we don't check the same index number over and over, We only need to check once of every element by using sliding window.
3. Space Complexity : O(1) - Constant auxiliary space is needed to save index of the range of window and to save currrent sum value, maximum sum value
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # range includes front and back index
        front = 0
        back = k-1

        cur_sum = sum(nums[front:back+1])
        max_sum = cur_sum
        while back < len(nums)-1:
            front += 1
            back += 1
            cur_sum = cur_sum + nums[back] - nums[front-1]
            max_sum = max_sum if max_sum > cur_sum else cur_sum

        return max_sum / k