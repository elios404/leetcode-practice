class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0  # 가장 높은 고도 (시작 고도가 0이므로 최소 0에서 시작)
        current = 0  # 현재 고도
        
        for g in gain:
            current += g                   # 다음 지점의 고도 계산
            highest = max(highest, current) # 최댓값 갱신
            
        return highest