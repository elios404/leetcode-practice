class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # 올림이 없으므로 바로 종료
            digits[i] = 0
            
        # 루프를 다 돌았는데도 return되지 않았다면 (예: [9, 9, 9] -> [0, 0, 0])
        return [1] + digits