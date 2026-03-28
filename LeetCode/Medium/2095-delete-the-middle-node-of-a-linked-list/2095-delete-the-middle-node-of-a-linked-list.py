"""
1. Approach :
    - Implemented the Fast and Slow Pointer (Tortoise and Hare) algorithm to locate the middle node in a single pass.
    - We initialize the `slow` pointer at the head, but give the `fast` pointer a head start (`head.next.next`). This mathematically guarantees that when `fast` terminates, `slow` stops exactly one node BEFORE the middle.
    - We then bypass the middle node by updating the `slow.next` pointer, effectively deleting it from the sequence in $O(1)$ auxiliary operations.
2. Time Complexity : $O(N)$ - A single traversal where the loop executes $N/2$ times, strictly optimizing the constant factor compared to a two-pass approach.
3. Space Complexity : $O(1)$ - Constant auxiliary space is utilized for the two pointer variables.
"""
# [Senior Pythonic Solution]
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list has only 0 or 1 node, deleting the middle leaves nothing.
        if not head or not head.next:
            return None
        
        # Senior Insight: Give 'fast' a head start so 'slow' lands right BEFORE the target.
        slow = head
        fast = head.next.next
        
        # Traverse until 'fast' reaches the end (handles both even and odd length lists)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 'slow' is now exactly the node before the middle. Delete the middle node.
        slow.next = slow.next.next
        
        return head