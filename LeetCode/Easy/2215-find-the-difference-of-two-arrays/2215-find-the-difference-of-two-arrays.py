"""
1. Approach :
    - Cast both input arrays into Hash Sets to instantly remove duplicates and prepare for mathematical operations.
    - Utilize Python's built-in set difference operator (`-`) to find elements exclusively present in one set but not the other.
2. Time Complexity : $O(N + M)$ - Set creation and set difference operations run in linear time relative to the sizes of the inputs.
3. Space Complexity : $O(N + M)$ - We require auxiliary memory to store the sets representing the unique elements of each array.
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)

        return [list(n1 - n2), list(n2 - n1)]