class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        use = k
        left = 0
        right = -1
        while right < len(nums)-1:
            if nums[right+1] == 1: # if next num is 1, widen to right
                right += 1
            else:
                if use > 0:
                    use -= 1
                    right += 1
                else:
                    cur = right - left + 1
                    ans = cur if cur > ans else ans

                    #move left until right can be moved again
                    while nums[left] == 1:
                        left += 1

                    # if nums[left] == 0
                    use += 1
                    left += 1

        # check after finish scanning array.
        cur = right - left + 1
        ans = cur if cur>ans else ans
        return ans