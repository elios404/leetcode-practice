#최대 두 번 까지 같은 숫자가 나올 수 있고, 추가 공간 없이 겹치는 숫자 제거, 오름차순으로 정렬된 것은 유지하기, 겹치는 것 제거하고 남은 k개를 평가함.
# 1. 오름차순으로 정렬 되어 있느니 같은 숫자가 몇 번 나오는지 확인하고 3개 이상일 때 부터 제거하면 된다.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        temp_num = nums[0]
        temp_count = 1
        removed = 0
        for i in range(1, len(nums)):
            if temp_num == nums[i]:
                temp_count += 1
                if temp_count >= 3:
                    nums[i] = 10**4+1
                    removed += 1
            else:
                temp_num = nums[i]
                temp_count = 1
        nums.sort()
        return len(nums)-removed