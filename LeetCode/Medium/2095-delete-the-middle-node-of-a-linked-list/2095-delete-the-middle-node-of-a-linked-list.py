# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0 # length of Linked List
        node = head
        while node:
            n += 1
            node = node.next

        #if n == 1:
            #return None
        
        idx = 0 # cur_node index
        target = n//2 - 1 # one before middle node
        cur_node = head
        while cur_node: # until last node
            if idx == target:
                break
            else:
                idx += 1
                cur_node = cur_node.next
        
        middle_node = cur_node.next
        cur_node.next = middle_node.next

        return head