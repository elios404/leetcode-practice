"""
1. Approach
    - Utilize a two-pass stratagy to compute prefix and suffix products without using division operator.
    - Instead of allocating separate arrays for prefixes and suffixes, accumulate the prefix products directry into result array during the fisrt forward pass.
    -During the second backward pass, maintain a ruunig `suffix` variable, multiplying it directly into the result array to achieve constant auxiliary space.
2. Time Complexity : O(N) - We perform exactly two linear passes over the input array.
3. Space Complexity : O(1) - The output array does not count towards auxiliary space, and we only use constant integer variables (`prefix` and `suffix`).
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

            
        