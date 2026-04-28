class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        duplicated_s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                duplicated_s.add(num)
        
        only_element = s-duplicated_s
        print(only_element)

        return list(only_element)[0]