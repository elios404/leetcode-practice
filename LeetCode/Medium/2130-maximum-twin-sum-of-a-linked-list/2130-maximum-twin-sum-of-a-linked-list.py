"""
1. Approach :
    - Step 1: Fast/Slow 포인터를 사용하여 리스트의 정확한 중간 지점을 찾습니다. (순회 횟수: N/2)
    - Step 2: 중간 지점부터 끝까지, 연결 리스트의 후반부 절반을 제자리에서(in-place) 뒤집습니다. (순회 횟수: N/2)
    - Step 3: 리스트의 시작점(head)과 뒤집힌 후반부의 시작점(prev)에서 동시에 출발하여, 두 값을 더하고 최대값을 갱신합니다. (순회 횟수: N/2)
2. Time Complexity : $O(N)$ - 총 1.5N 번의 루프 실행으로 선형 시간을 보장합니다.
3. Space Complexity : $O(1)$ - 배열을 생성하지 않고, 기존 노드들의 포인터 방향만 조작하므로 추가 메모리가 전혀 들지 않습니다.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Fast & Slow 포인터로 중간 지점 찾기
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 루프가 끝나면 slow는 정확히 후반부 절반의 시작점에 위치합니다.
        
        # Step 2: 후반부 절반 뒤집기 (황금 템플릿 적용)
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 루프가 끝나면 prev는 원래 리스트의 마지막 노드이자, 뒤집힌 후반부 리스트의 '새로운 시작점(head)'이 됩니다.
        
        # Step 3: 양 끝에서부터 동시에 전진하며 최대 합 구하기
        max_sum = 0
        first_half = head
        second_half = prev # 뒤집힌 절반의 시작점
        
        while second_half: # 후반부 리스트가 끝날 때까지만 순회
            # 내장 함수명(max, sum) 섀도잉 방지를 위해 변수명 변경
            current_sum = first_half.val + second_half.val
            if current_sum > max_sum:
                max_sum = current_sum
                
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum