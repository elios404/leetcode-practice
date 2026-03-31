# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        value = [] #use O(N) space complexity to solve this problem.

        # O(N) time
        cur_node = head
        while cur_node:
            value.append(cur_node.val)
            cur_node = cur_node.next
        
        n = len(value)
        max = 0
        # O(N) time, more exactly O(n/2) time
        for i in range(n//2):
            sum = value[i] + value[n-1-i]
            if sum > max:
                max = sum
        
        return max