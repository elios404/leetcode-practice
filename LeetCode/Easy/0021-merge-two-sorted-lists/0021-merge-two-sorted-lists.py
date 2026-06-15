# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        curr1 = list1
        curr2 = list2
        if curr1.val <= curr2.val:
            start = curr1
            curr1 = curr1.next
        else:
            start = curr2
            curr2 = curr2.next

        ret = start
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                ret.next = curr1
                ret = ret.next
                curr1 = curr1.next
            else:
                ret.next = curr2
                ret = ret.next
                curr2 = curr2.next
        
        if not curr1: #finished list1
            ret.next = curr2
        else:
            ret.next = curr1
        
        return start