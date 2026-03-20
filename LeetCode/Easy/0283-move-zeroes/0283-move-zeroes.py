"""
1. Approach
    - Utilize a Fast/Slow Two-Pointer approach to partition the array in-place.
    - As teh loop iterates, whenever a non-zero element is found, it is swapped with the element at the `insert_pos` (the slow pointer).
    - The `insert_pos` is then incremented, guaranteering that all elements to the left of `insert_pos` are non-zero, and all zeros are natually pushed to the rigth.
2. Time Complexity : O(N) - A single linear traversal of the array
3. Space Complexity : O(1) - In-place modification using a single integer pointer variable.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1