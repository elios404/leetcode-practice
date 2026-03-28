# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_half_node = None #one before half node actually
        cur_node = head

        idx = 0 #pointing cur_node
        while cur_node:
            if idx == 1:
                prev_half_node = head
            elif idx % 2 == 1:
                prev_half_node = prev_half_node.next
            idx += 1
            cur_node = cur_node.next
        
        if not prev_half_node: # when lenght is 1
            return None

        half_node = prev_half_node.next
        prev_half_node.next = half_node.next

        return head
