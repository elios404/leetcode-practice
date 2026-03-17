"""
1. Approach
    - Firstly, should not use `/`operator. nums.length <= 10^5, so normally if a problem gives us 1s, then we need to implement O(N log N) algorithm.
    - If we can use `/` then it's easy. Just multiple all the numbers in the list and divide each elements to total mul value. O(2*N) time complexity. O(1) space complexity.
    - Calculate in advance the value of 1th ~ ith and also Nth ~ ith order and if I want to find k th value, use (1th~(k-1)th) * ((k+1)th ~ Nth) 
2. Time Complexity : O(N) - itereate for three times, O(3*N)
3. Space Complexity : O(N) - 3 arryas which length is N are needed.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] 
        n = 1
        for num in nums:
            n *= num
            l.append(n)
        
        reverse_l = [1]  
        n = 1
        for num in reversed(nums):
            n *= num
            reverse_l.append(n)
        
        length = len(nums)
        ret = []
        for i in range(length):
            # one small problem is that I can't fully understand the index of the list
            ret.append(l[i] * reverse_l[length-i-1])
        return ret

            
        