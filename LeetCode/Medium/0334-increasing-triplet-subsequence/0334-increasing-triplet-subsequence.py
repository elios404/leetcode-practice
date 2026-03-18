"""
1. Approach
    - Using LCS finding algorithm method.
2. Time Complexity : O(N) - iterate List num and in iteration, need to iterate `l` to find idx, but maximum length of `l` is 3 so it's constant value. So O(3N) can be O(N)
3. Space Complexity : O(1) - We need auxiliary space for list `l` but maximum length of `l` is 3 so, we need constant auxiliary space.
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = []
        for num in nums:
            if len(l) == 0: 
                l.append(num)
                continue
            
            if len(l) == 3:
                return True
            
            if num > l[-1]:
                l.append(num)
            else:
                # part I spend time to solve, difficult
                idx = len(l) - 2
                while num <= l[idx] and idx != -1:
                    idx -= 1
                l[idx+1] = num
        
        return len(l)>=3

        