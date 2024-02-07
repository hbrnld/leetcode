# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        mid, end = head, head
        mx = 0

        # Get middle of linked list
        while end and end.next:
            mid = mid.next          # Slow
            end = end.next.next     # Fast

        # Reverse the second half
        curr, prev = mid, None
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Find the maximum pair sum
        while prev:
            mx = max(mx, head.val + prev.val)
            head, prev = head.next, prev.next
        
        return mx