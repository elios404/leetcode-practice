# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 가짜 시작 노드(Dummy Node) 생성
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # l1, l2, carry 중 하나라도 남아있으면 계속 실행!
        while l1 or l2 or carry:
            # 1. 노드가 없으면 0으로 처리
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 2. 합계 계산
            total = val1 + val2 + carry
            carry = total // 10

            # 3. 계산된 결과로 즉흥적으로 next 노드를 만들어서 연결!
            curr.next = ListNode(total % 10)
            curr = curr.next  # 포인터 이동

            # 4. 다음 노드가 있는 경우에만 이동
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # dummy 다음 노드부터가 진짜 정답 리스트
        return dummy.next