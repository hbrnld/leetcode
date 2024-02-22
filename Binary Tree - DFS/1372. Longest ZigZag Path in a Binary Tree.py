# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.zigzag(root, 's', 0, 0)

    def zigzag(self, node, curr, prev, cnt): 
        if not node:
            return cnt
        elif curr == 's': 
            cnt = 0
        elif curr != prev: 
            cnt += 1
        else: 
            cnt = 1
        
        return max(self.zigzag(node.left, 'l', curr, cnt), self.zigzag(node.right, 'r', curr, cnt))
