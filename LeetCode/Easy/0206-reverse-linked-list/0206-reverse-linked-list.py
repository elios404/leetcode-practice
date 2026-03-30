# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur_node = head.next
        prev_node = head
        head.next = None # make it as end
        while cur_node:
            next_node = cur_node.next # save next_node object
            cur_node.next = prev_node
            prev_node = cur_node

            head = cur_node
            cur_node = next_node

        return head