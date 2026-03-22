"""
1. Approach :
    - Implement a dynamic sliding window using a fast/slow pointer technique.
    - The `right` pointer iterates through the array, expanding the window and tracking the count of zeroes encountered.
    - If the zero count exceeds our allowance `k`, the window is invalid. We enter a `while` loop to advance the `left` pointer, discarding elements until the zero count drops back to a valid state.
    - Once the window is guaranteed to be valid, we calculate the current length and update the global maximum.
2. Time Complexity : $O(N)$ - Both the `left` and `right` pointers only move forward, visiting each element at most twice.
3. Space Complexity : $O(1)$ - Constant auxiliary space is utilized for pointer and counter variables.
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        # The 'right' pointer expands unconditionally
        for right in range(len(nums)):
            # Update our state
            if nums[right] == 0:
                zero_count += 1
                
            # If our state is invalid, shrink from the left until it's valid
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            # At this point, the window is mathematically guaranteed to be valid.
            # Calculate the length and update the maximum.
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len