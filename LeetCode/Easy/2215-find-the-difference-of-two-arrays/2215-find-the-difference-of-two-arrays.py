"""
1. Approach
    - To find integers which are not in another list, use set data structure to make integer distinctable and filter as we want
2. Time Complexity : O(N) - To make list to set, O(N) and to make a result list, iterate n1, n2 sets, O(N) and to check whether elements are in the another set, O(1)
3. Space Complexity : O(N) - Except auxiliary space for returning, sets n1, n2 are needed, O(2 * N)
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)

        res1 = list(num for num in n1 if num not in n2)
        res2 = list(num for num in n2 if num not in n1)

        return [res1, res2]