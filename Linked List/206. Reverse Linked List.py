# https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None

        while head: 
            next = head.next        # Set next node
            head.next = prev        # Update pointer to previous node

            prev = head             # Move prev forward
            head = next             # Move head forward

        return prev