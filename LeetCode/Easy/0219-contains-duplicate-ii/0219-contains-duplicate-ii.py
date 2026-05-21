""" 
1. Approach
    - Make it as a dictionary which contains number and the indexs list of that number.
    - So in certain number, don't need linear traversal of the whole list, just compare with the most closest same number index
2. Time Complexity : O(N) - In worst case, can be O(N^2) but not very sure.
3. Space Compplexity : O(N) -  Every number in the list can be the key so O(N), and idx continues until lenght of the list O(N) so O(2N)
4.Edge Case: Before Submission think about the Edge Case
    - If nums is empty, then not goes into for loof, return False
    - If K == 0, then return False 
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False # not distinct indices or can't find 
        last_seen = {}

        # O(N)
        for i, num in enumerate(nums):
            if num in last_seen and i - k <= last_seen[num]:
                return True
            last_seen[num] = i # replace into most closest.
         
        return False