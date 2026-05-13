"""
1. Approach
    - numbers are already sorted in accending order. So by choosing each two ends of the list, if sum of numbers are smaller than target then it should be bigger, so move left index to one right. Opposite situation are same
    - Because there is exactly one solution, so it's garunted to find the answer when sum is small then move left to one right, and if it's bigger than target then move right to one left.
2. Time Complexity : O(N) -  In worst case, linear scan of numbers.
3. Space Comeplexity : O(1) - Const auxiliary space needed, just need left_idx, and right_idx
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left_idx, right_idx = 0, n-1

        while left_idx < right_idx:
            val = numbers[left_idx] + numbers[right_idx]

            if val == target:
                return [left_idx+1, right_idx+1]
            elif val < target:
                left_idx += 1
            else:
                right_idx -= 1

        return None