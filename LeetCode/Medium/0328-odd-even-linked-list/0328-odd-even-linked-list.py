# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_head = head
        odd_node = odd_head
        even_head = head.next
        even_node = even_head

        isOdd = True
        cur_node = head.next.next # start from 3rd node
        while cur_node: #until cur_node goes to end
            print(cur_node.val)
            if isOdd:
                odd_node.next = cur_node
                odd_node = cur_node
            else:
                even_node.next = cur_node
                even_node = cur_node
            isOdd = not isOdd
            cur_node = cur_node.next
        
        odd_node.next = even_head
        even_node.next = None

        return odd_head