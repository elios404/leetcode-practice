# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()

        curr_l1 = l1
        curr_l2 = l2
        curr = result
        carry = 0

        while curr_l1 and curr_l2: #when both has value
            sum_val = curr_l1.val + curr_l2.val + carry
            curr.val = sum_val % 10
            carry = sum_val // 10

            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
            if curr_l1 or curr_l2:
                curr.next = ListNode()
                curr = curr.next

        if curr_l1:
            node = curr_l1
        else:
            node = curr_l2
        
        while node:
            curr.val = (node.val + carry) % 10
            carry = (node.val + carry) // 10

            node = node.next
            if not node:
                break
            curr.next = ListNode()
            curr = curr.next
        
        if carry != 0:
            curr.next = ListNode()
            curr.next.val = carry

        return result