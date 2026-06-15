class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as the anchor
        dummy = ListNode()
        curr = dummy

        # Re-use list1 and list2 directly as our traversing pointers
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Attach whatever is remaining. If list1 is exhausted, it attaches list2 (and vice versa)
        curr.next = list1 if list1 else list2
        
        return dummy.next